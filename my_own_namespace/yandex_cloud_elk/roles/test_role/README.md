# test_role

Single-task роль, использующая модуль `my_test` для создания/обновления текстового файла.

---

## 🔧 Переменные

- `test_role_path` — путь к файлу (по умолчанию `/tmp/test_role.txt`).
- `test_role_content` — содержимое (по умолчанию `"Привет! Это файл, созданный ролью test_role."`).

---

## 📘 Пример использования

```yaml
- hosts: localhost
  connection: local
  gather_facts: false
  collections:
    - my_own_namespace.yandex_cloud_elk
  roles:
    - test_role
