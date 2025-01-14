## What is EDS/EDA ?

Event driven solution or architecture defines a real-time communication between systems generally in a asynchronous way. It uses -

- Publish-Subscriber Pattern
- Event streaming 

It signifies independent components, which can be developed, deployed, and scaled independently, not tightly coupled.

**Representation**: Events are expressed as messages or signals that communicate specific information.

**Triggering**: Various sources, such as user actions or data changes, can trigger events.

**Asynchronicity**: EDA often uses asynchronous communication, allowing components to work independently and in parallel.

**Publish-Subscribe Model**: A publish-subscribe model is used to manage events, with individuals who produce them publishing them and interested parties subscribing to them.

**Event Handling**: Components have specific handlers that dictate their response to events.

**Real-Time Processing**: Events allow immediate reactions to changes, making EDA ideal for scenarios requiring quick responsiveness.

## Why EDS/EDA ?
- Flexibility and Responsiveness - quickly adjust to changing situations
- Scalability - components can be added or removed without affecting the current configuration
- Real-time Processing
- Decentralized Communication

## Architecture of EDA
Key components can be enlisted--

- Event Source: Any system or component that generates events. 
- Event: Significant occurrences or changes in state.
- Event Broker/Event Bus: It handls event distribution, filtering, and routing.
- Publisher: Generates and sends events to the event bus.
- Subscriber: Listen for relevant events on the event bus and take action accordingly.
- Event Handler: How to process received events.
- Dispatcher: Route events to the appropriate event handlers.
- Aggregator: Several related events are combined by an aggregator to create a single, more significant event.
- Listener: Actively monitors the event bus for events and reacts to them.


## Useage
- real-time application
- scalability needs
- Independent components
- Complex event response
- Integration of Diverse system


## Key Benifits
enhances flexibility, 
scalability, 
real-time responsiveness 
Loose coupling 
Enhanced Modularity

## Challanges
- Complexity
- Event order, consistency
- Debug, track
- Latency
## Alternatives

## Exampls
E-commerce site
Iot
Telecommunications

[Reference 1](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven)
[Reference 2](https://www.geeksforgeeks.org/event-driven-architecture-system-design/)