# wifi-menu
PyQt gui to connect to different wifi networks.

## Usage

Run with sudo permissions. Currently the easiest way to run this is by adding the project folder to your `PATH`, for example:

```bash
PATH=$PATH:$HOME/wifi-menu/
```

Also make sure the main python file (`wifi-menu`) is executable.

A sample configuration file is provided in the project root directory.  This must be renamed to `config.json` to use the app. None of the fields actually have to be set.  The `default_interface` parameter has to be manually set to your preferred wireless interface name.  Network configurations can be added in the app itself.

## TODO:
- ask for sudo password (if needed) from within application, without relying on terminal
