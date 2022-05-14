---
title: Importing Classes
date: 2021-10-14 05:33
tags:
- #python
---

Just like with builtin modules or modules that other's have build you can import
your own groups of classes the same way.

## Importing Classes

### Importing a single class

Always include a docstring at the head of a module you create.

You can import modules just like with any other module.

```python
from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

```
2019 Audi A4
This car has 23 miles on it.
```

### Storing multiple classes in a module

You can store as many classes as you like in a module, but they should be
related. 

### You can import multiple classes

```python
from car import Car, ElectricCar
...
```

### Or you can import the entire module

```python
import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
...
```

### Importing all classes from a Module

Use `*` syntax:

```python
from module_name import *
```

This method is discouraged though. It's better to know what's imported based on
the import statement at the head of the file.

## Importing a Module into a Module

Sometimes modules depend on other modules, so you can just import that module
into the other module using the same syntax:

```python
from car import Car

Some classes that depend on car...
```

## Using Aliases

```python
from electric_car import ElectricCar as EC
```


