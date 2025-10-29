from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random

Base = declarative_base()

student_course = Table(
    "student_course", Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True),
)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    courses = relationship("Course", secondary=student_course, back_populates="students")

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    students = relationship("Student", secondary=student_course, back_populates="courses")


engine = create_engine("sqlite:///students.db", echo=True)
SessionLocal = sessionmaker(bind=engine)

if __name__ == "__main__":
    Base.metadata.create_all(engine)

    # Створюємо курси
    with SessionLocal() as session:
        if session.query(Course).count() == 0:
            session.add_all(Course(title=f"Course {i}") for i in range(1, 6))
            session.commit()
            print("✅ Курси створені!")

    # Додаємо 20 студентів і робимо розподіл по 1–3 курсах
    with SessionLocal() as session:
        if session.query(Student).count() == 0:
            names = [f"Student{i}" for i in range(1, 21)]
            all_courses = session.query(Course).all()
            for name in names:
                s = Student(name=name)
                s.courses = random.sample(all_courses, random.randint(1, 3))
                session.add(s)
            session.commit()
            print("✅ Студенти створені!")

    # приклади запитів
    with SessionLocal() as session:
        # Хто на курсі 1
        c1 = session.get(Course, 1)
        print(f"\nСтуденти на {c1.title}:")
        for st in c1.students:
            print("–", st.name)

        # На яких курсах Student1
        st1 = session.get(Student, 1)
        print(f"\nКурси {st1.name}:")
        for c in st1.courses:
            print("–", c.title)

    # (4) Оновлення та видалення
    with SessionLocal() as session:
        st = session.get(Student, 1)
        if st:
            before = st.name
            st.name = "Незабудько"
            session.commit()
            print(f"\n✏️ Ім'я змінено: {before} → {st.name}")

        st2 = session.get(Student, 2)
        if st2:
            print("🗑️ Видаляємо:", st2.name)
            session.delete(st2)
            session.commit()
            print("✅ Студента видалено")
