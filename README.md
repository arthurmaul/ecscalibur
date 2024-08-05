# ECSCALIBUR development engine
## INTRODUCTION
### The Why

### The What

### The How

## DOCS
### For Users

### For Contributors

## REFERENCE
### Modules
| type | description |
| --- | --- |
| app       | runs the main loop, triggering the dispatch of the broker and then running phases |
| editor    | contains all the interfaces for interacting with the engine via the app |
| schedules | handles the ordering and registration of system functions into phases |
| events    | handles the delegation of window or custom events to assigned handlers |
| math      | classes to handle vectors, matrices, and other mathematical primitives, as well as calculations |
| physics   | forces, rigid bodies, and colliders |
| graphics  | text, sprites, spritegroups, spritesheets, and an animation player |
| models    | the entity, tag, relationship, and component models, and its associated functionality |
| prefabs   | built in components, just as a 2d controller|

| model type | description |
| --- | --- |
|world | the entity, component, relation, and other constructors |
|commands | the setters and markers |
|query | the query builders and helper functions |

## IDEAS
- text based buttons with the background turning white or another color when hovered over
- serialization too and from json based on blueprints, converting entities to blueprints and vice versa, as well as any components they need
- component registered so a blueprint can be passed to the factory and referenced later
- world[actor].set[component](*args, **kwargs)
