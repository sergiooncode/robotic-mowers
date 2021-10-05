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

## Considerations

In the last commit (probably too large I have to admit although I think the intention is clear) the code structure
necessary for the next stage of the kata development is introduced, that is, putting the robotic mower in a factory
map with physical constrains (size and obstacles). Up to that commit the code, although being according to
specifications, didn't have all the right abstractions and relied too much in basic strings for orientations, instructions, etc.