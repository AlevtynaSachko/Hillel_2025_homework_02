# test_cars_api.py
import pytest
import allure


@pytest.mark.usefixtures("api_session")
@allure.feature("Cars API: пошук/сортування")
class TestCarsSearch:

    @pytest.mark.parametrize(
        "sort_by, limit, expect_order",
        [
            ("price", 3, "asc_numeric"),
            ("year", 5, "asc_numeric"),
            ("engine_volume", 10, "asc_numeric"),
            ("brand", 4, "asc_string"),
            (None, 7, "asc_string_default_brand"),
            ("nonexistent", 6, "insertion_order"),
        ],
        ids=[
            "sort_by_price_limit_3",
            "sort_by_year_limit_5",
            "sort_by_engine_volume_limit_10",
            "sort_by_brand_limit_4",
            "no_sort_by_defaults_to_brand_limit_7",
            "unknown_sort_field_insertion_order_limit_6",
        ],
    )
    def test_cars_parametrized(self, sort_by, limit, expect_order):
        # Step 1: підготувати query params
        with allure.step("Підготувати query params"):
            params = {}
            if sort_by is not None:
                params["sort_by"] = sort_by
            if limit is not None:
                params["limit"] = limit

        # Step 2: зробити запит до /cars
        with allure.step(f"GET /cars з params={params}"):
            url = f"{self.base_url}/cars"
            self.logger.info("GET %s params=%s", url, params)
            resp = self.session.get(url, params=params)
            self.logger.info(
                "Відповідь /cars: %s | %s байт",
                resp.status_code,
                len(resp.content),
            )
            # прикріпимо тіло відповіді для зручного дебага у звіті
            try:
                allure.attach(resp.text, "cars_response.json", allure.attachment_type.JSON)
            except Exception:
                allure.attach(resp.text, "cars_response.txt", allure.attachment_type.TEXT)

        # Step 3: перевірити статус-код
        with allure.step("Перевірити статус-код 200"):
            assert resp.status_code == 200, f"Невдалий статус: {resp.status_code}"

        # Step 4: розпакувати body
        with allure.step("Розпакувати JSON-відповідь"):
            data = resp.json()

        # Step 5: перевірити ліміт
        with allure.step(f"Перевірити ліміт результатів = {limit}"):
            if limit is not None:
                assert len(data) == limit, f"Очікували {limit}, отримали {len(data)}"

        # Step 6: перевірити порядок сортування
        with allure.step(f"Перевірити порядок сортування: {expect_order}"):
            if expect_order == "asc_numeric":
                vals = [item[sort_by] for item in data]
                assert vals == sorted(vals), f"Очікували ↑ за {sort_by}, маємо {vals}"

            elif expect_order == "asc_string":
                brands = [item["brand"] for item in data]
                assert brands == sorted(brands), f"Очікували A→Z за brand, маємо {brands}"

            elif expect_order == "asc_string_default_brand":
                brands = [item["brand"] for item in data]
                assert brands == sorted(brands), f"Очікували дефолтне A→Z за brand, маємо {brands}"

            elif expect_order == "insertion_order":
                # для невідомого поля ключ сортування дорівнює 0 -> вихідний порядок із БД
                assert data[0]["brand"] == "BMW", f"Очікували першим 'BMW', маємо {data[0]['brand']}"
            else:
                pytest.fail(f"Невідоме очікування порядку: {expect_order}")
