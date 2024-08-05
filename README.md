# ECSCALIBUR development engine
## INTRODUCTION
### The Why
many existing tools, while often sufficient for many and beautifully architected and implemented, could be improved upon. specifically:
- they are often too complex for many to adopt easily (unreal)
- they require learning a bespoke scripting language with low skill transference (godot and gdscript)
- they box you into an ecosystem or payment model (unity)
- they are too low level (raylib or panda3d)
- they are too specialized for general use (rpgmaker)
- difficulty of modification or of augmentation to the engine or the game (most of the above, and many more)

### The What
- a simple set of tools to ensure easy adoption
- general purpose programming languages for the front and back end to ensure knowledge transference both to and from the engine
- the engine built into the game instance with minimal boilerplate. ships as is, games come first, modding comes standard
- simple source code to encourage understanding and customization in alignment with individual needs
- high level tooling for simple and easy development

### The How
- a c++ backend and a python front end, allowing both speed and high level expressiveness for the user
- an archetypal ecs using well known and understood terminology to make use intuitive and straight forward for modders and developers
- the game launches as an empty instance, with the engine as a built in features accessed in game with a "dev-code" you can set
- clearly defined and easy to use primitives, and holistic documentation
- free and open source, freedom is guanrenteed and ensured for the lifetime of your projects

## DOCS
### For Users
todo...

### For Contributors
todo...

## REFERENCE
### TODO
- [ ] 1.0.0.Alpha
    - [X] Running app
    - [ ] Built in editor with a code editor and a project, scene, and object editor
    - [X] Built in schedules with a simple registration interface
    - [X] Event handling interface with priority events directly sent as well as deferral and batch processing
    - [X] Key binding functionality to detect presses and call respective handler functions
- [ ] 1.1.0.Beta
    - [ ] ...

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

### Models
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
