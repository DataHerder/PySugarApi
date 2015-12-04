# PySugarApi
## SugarCRM API Implementation in Python 2.7
### A simple wrapper

This application is a very simple wrapper that handles logging in via Python.

Dependencies include: requests, pprint, json, hashlib and collections

```python
Sg = PySugarApi('username', 'password', 'http://your/instance/url')
req = Sg.post('get_entries', {
  'session': Sg.session_id,
  'module_name': 'Accounts',
  'ids': 'account-id',
  'select_fields': [],
  'unified_search_only': False,
  'favorites': False,
  'filter': array(),
});
```
