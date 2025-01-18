# What is Cloud Native?

Cloud native is a system architecture pattern that focus on taking maximum advantage of cloud computing. These techniques enable loosely coupled systems that are resilient, easily manageable, and observable. It allows engineers, developers to make high-impact changes frequently and predictably with minimum toil.[1]

# Benifits
**Faster development**
Developers use the cloud-native approach to reduce development time and achieve better quality applications. Instead of relying on specific hardware infrastructure, developers build ready-to-deploy containerized applications with DevOps practices. This allows developers to respond to changes quickly. For example, they can make several daily updates without shutting down the app. 

**Platform independence**
By building and deploying applications in the cloud, developers are assured of the consistency and reliability of the operating environment. They don't have to worry about hardware incompatibility because the cloud provider takes care of it. Therefore, developers can focus on delivering values in the app instead of setting up the underlying infrastructure. 

**Cost-effective operations**
You only pay for the resources your application actually uses. For example, if your user traffic spikes only during certain times of the year, you pay additional charges only for that time period. You do not have to provision extra resources that sit idle for most of the year.[2]

# Key Ideas
## Containers
Containers are a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries, and settings. Containers isolate software from its environment and ensure that it works uniformly despite differences for instance between development and staging. Containers are a key component of cloud-native applications because they enable developers to build, package, and deploy applications consistently across different environments. Containers are also portable, scalable, and easy to manage, making them ideal for modern cloud-native applications.
## Service Meshes
A service mesh is a mechanism for managing communications between the various individual services that make up modern applications in a microservice-based system.
The service mesh decouples the network logic from application or business logic of each microservice so that it can be implemented and managed independently across the whole system. When a service mesh is applied, all inter-service communication is routed through its proxies, which can be used to implement networking features such as encryption and load balancing. The insfrastructure layer of service mesh is a sort of alternative to API gateway but handles only communication between services. While the service mesh pattern was designed to handle network connectivity between microservices, it can also be applied to other architectures (monolithic, mini-services, serverless).[3]
## Microservices
Microservices are a software development technique—a variant of the service-oriented architecture (SOA) architectural style that structures an application as a collection of loosely coupled services. In a microservices architecture, services are fine-grained and the protocols are lightweight. The benefit of decomposing an application into different smaller services is that it improves modularity and makes the application easier to understand, develop, test, and become more resilient to architecture erosion. It parallelizes development by enabling small autonomous teams to develop, deploy and scale their respective services independently. It also allows the architecture of an individual service to emerge through continuous refactoring. Microservices-based architectures enable continuous delivery and deployment.
## Immutable infrastructure
Immutable infrastructure is an approach to managing services and software deployments on IT resources by replacing the entire infrastructure for each deployment, rather than making changes in-place. This technique is used to ensure that infrastructure is consistent and predictable. It also helps to prevent configuration drift and ensure that the infrastructure is in a known good state. Immutable infrastructure is a core concept in DevOps and is seen as a way to ensure that infrastructure is more reliable and easier to manage.
## Declarative API
A declarative API is an interface that allows developers to describe the desired state of their applications and infrastructure, rather than the steps needed to get there. This approach is used to simplify the management of complex systems by allowing developers to focus on what they want to achieve, rather than how to achieve it. Declarative APIs are used in cloud-native applications to define the desired state of the application, infrastructure, and services, and to automatically manage the deployment, scaling, and configuration of these resources.
# Challanges
The cloud-native approach is not without its challenges. Some of the key challenges include:
- Complexity: Cloud-native applications can be complex to design, build, and manage, especially when they involve multiple services, containers, and microservices. This complexity can make it difficult to troubleshoot issues and ensure the reliability and security of the application.
- Security: Cloud-native applications can be more vulnerable to security threats than traditional applications, due to the distributed nature of the application, the use of containers and microservices, and the reliance on third-party services and APIs. Securing cloud-native applications requires a comprehensive approach that includes encryption, access control, monitoring, and auditing.
- Scalability: Cloud-native applications are designed to be highly scalable, but achieving this scalability can be challenging, especially when the application involves multiple services, containers, and microservices. Ensuring that the application can scale up and down dynamically, handle spikes in traffic, and maintain performance under heavy load requires careful planning and design.
- Monitoring and observability: Cloud-native applications generate large amounts of data, logs, and metrics, which can make it difficult to monitor and troubleshoot issues. Ensuring that the application is observable, with the right monitoring tools and dashboards in place, is essential for maintaining the reliability and performance of the application.
- Cost: Cloud-native applications can be more expensive to build and operate than traditional applications, due to the use of containers, microservices, and third-party services. Managing costs, optimizing resource usage, and ensuring that the application is cost-effective to run are key challenges for organizations adopting the cloud-native approach.


# Practical Area
Some of the practical areas where cloud-native technologies are being used include:
- Web applications
- Mobile applications
- Internet of Things (IoT)
- Big data
- Machine learning










# Reference
[1]: [Cloud Native Computing Foundation](https://www.cncf.io/)
[2]: [Amazon - What is cloud native](https://aws.amazon.com/what-is/cloud-native)
[3]: [Service Mesh](https://konghq.com/blog/learning-center/what-is-a-service-mesh)
