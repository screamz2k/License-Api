# License-API
Licensing-API is an API to create, manage and check keys for your projects.

## Features
- Web Interface
- Create/Delete/Activate/Deactivate Keys over WI or API
- Login
- Signup
- Password Fernet Encryption
- Automatic Key Counter 
## What's not covered?
- Anti-Bruteforce-Defence
- Sql-Injection (not-tested)
- Api-Limit
# Explanation
I'm just a junior backend dev, and wasn't able to cover these protections,
because of missing Knowledge and this Project was made in 5 days, and I want to go on.
# Setup
1. Open a terminal 
2. Clone Repo
    - ``cd (your folder)``
    - ``git clone https://github.com/screamz2k/License-API``
3. Run setup
    - ``python3 setup.py``

# Docs
``* Login required.``

## *Create Key
### [GET] ``/api/create-key``
``?expiry=30``<br>
Set Days the key is valid after activation.

### [POST] ``/api/create-key``
```
{
"expiry": 30,
"username": your-username,
"password" your-password
}
```
## *Create multiple Keys
### [GET] ``/api/create-keys``
``?expiry=30``<br>
Set Days the keys are valid after activation.<br>
``?amount=30``<br>
Set Amount of keys to generate.
### [POST] ``/api/create-key``
```
{
"amount": 10,
"expiry": 30,
"username": your-username,
"password" your-password
}
```
## *Delete Key
### [GET] ``/api/delete-key``
``?key=your-key``<br>
Set the key you want to delete.<br>
### [POST] ``/api/delete-key``
```
{
"key": your-key,
"username": your-username,
"password" your-password
}
```
## Activate Key
### [GET] ``/api/activate-key``
``?key=your-key``<br>
Set the key you want to activate.<br>
``?mac=clients-mac-address``<br>
Set the mac-address of the client to prevent cracking.<br>
### [POST] ``/api/activate-key``
```
{
"key": your-key,
"mac": clients-mac-address
}
```
## *Deactivate Key
### [GET] ``/api/deactivate-key``
``?key=your-key``<br>
Set the key you want to deactivate.<br>
### [POST] ``/api/deactivate-key``
```
{
"key": your-key,
"username": your-username,
"password": your-password
}
```
## Check Key Data
### [GET] ``/api/check-key``
``?key=your-key``<br>
Set the key you to check.<br>