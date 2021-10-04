# robotic-mowers

To run the tests, and in order not to leave a messy local environment in the host where they are run,
a Docker container is used. A base Dockerfile is provided with the Python dependencies used in the project
which should only be used once to build, and a development Dockerfile which should be used to build
when the source code or the tests are changed.

## Build base image

```
make build-base
```

## Build developement image

```
make build
```

## Run tests

```
make tests
```