# luigi-example

Luigi example project.

To run, use 

```
rm -rf /tmp/bar/
PYTHONPATH='.' luigi --module examples.foo examples.Foo --workers 2 --local-scheduler
```
