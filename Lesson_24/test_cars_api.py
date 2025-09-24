import pytest

@pytest.mark.usefixtures("api_session")
class TestCarsSearch:

    @pytest.mark.parametrize(
        "sort_by, limit, expect_order",
        [
            # валідні поля сортування
            ("price", 3, "asc_numeric"),
            ("year", 5, "asc_numeric"),
            ("engine_volume", 10, "asc_numeric"),
            ("brand", 4, "asc_string"),
            # без sort_by — очікуємо сортування за brand
            (None, 7, "asc_string_default_brand"),
            # неіснуюче поле — лишається вихідний вставний порядок
            ("nonexistent", 6, "insertion_order"),
        ],
        ids=[
            "sort_by_price_limit_3",
            "sort_by_year_limit_5",
            "sort_by_engine_volume_limit_10",
            "sort_by_brand_limit_4",
            "no_sort_by_limit_7_defaults_to_brand",
            "unknown_sort_field_insertion_order_limit_6",
        ],
    )
    def test_cars_parametrized(self, sort_by, limit, expect_order):
        params = {}
        if sort_by is not None:
            params["sort_by"] = sort_by
        if limit is not None:
            params["limit"] = limit

        url = f"{self.base_url}/cars"
        self.logger.info("GET %s params=%s", url, params)
        resp = self.session.get(url, params=params)
        self.logger.info("Відповідь /cars: %s | %s байт", resp.status_code, len(resp.content))

        assert resp.status_code == 200, f"Невдалий статус: {resp.status_code}"
        data = resp.json()

        # Перевірка ліміту
        if limit is not None:
            assert len(data) == limit, f"Очікували {limit} елемент(ів), отримали {len(data)}"

        # Перевірка порядку
        if expect_order == "asc_numeric":
            vals = [item[sort_by] for item in data]
            assert vals == sorted(vals), f"Очікували зростаюче сортування за {sort_by}, маємо {vals}"

        elif expect_order == "asc_string":
            brands = [item["brand"] for item in data]
            assert brands == sorted(brands), f"Очікували алфавітне сортування за brand, маємо {brands}"

        elif expect_order == "asc_string_default_brand":
            # коли sort_by=None — додаток сортує за brand
            brands = [item["brand"] for item in data]
            assert brands == sorted(brands), f"Очікували дефолтне сортування за brand, маємо {brands}"

        elif expect_order == "insertion_order":
            # для невідомого поля ключ сортування дорівнює 0 -> порядок збігається з вихідною БД
            # Перевіримо хоча б перші елементи за відомими даними (BMW має бути першим)
            assert data[0]["brand"] == "BMW", f"Очікували першим 'BMW', маємо {data[0]['brand']}"
        else:
            pytest.fail(f"Невідоме очікування порядку: {expect_order}")
