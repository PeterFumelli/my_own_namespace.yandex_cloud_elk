# Ansible Collection: my_own_namespace.yandex_cloud_elk

Учебная Ansible-коллекция, созданная для практики написания собственных модулей и ролей.
Содержит пример простого модуля `my_test` и роли `test_role`.

---

## 📦 Состав коллекции

### 🔹 Модуль `my_test`

Создаёт или обновляет текстовый файл на целевой машине по указанному пути.

**Параметры:**

- `path` *(str, required)* — путь к файлу.
- `content` *(str, required)* — содержимое файла.

**Возвращает:**

- `changed` (bool) — был ли изменён файл.
- `path` (str) — путь к файлу.
- `content` (str) — содержимое.

**Пример:**

```yaml
- hosts: localhost
  connection: local
  tasks:
    - name: Create file
      my_own_namespace.yandex_cloud_elk.my_test:
        path: /tmp/hello.txt
        content: "Hello from module"
