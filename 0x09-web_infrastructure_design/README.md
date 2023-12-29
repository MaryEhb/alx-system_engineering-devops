# 0x09. Web Infrastructure Design

## [0. Simple Web Stack](https://github.com/MaryEhb/alx-system_engineering-devops/tree/main/0x09-web_infrastructure_design/0-simple_web_stack)

### Introduction
This repository contains the design for a simple web infrastructure that hosts a website reachable via www.foobar.com. The infrastructure is composed of a single server utilizing a LAMP stack.

### Domain Name Resolution Process
1. **User Enters URL:**
   - The user initiates the process by typing the URL of a regular website into the browser.

2. **Browser Cache Lookup:**
   - The browser checks its cache to determine if it already possesses the IP address corresponding to the entered domain name.

3. **Operating System Cache Lookup:**
   - If the IP address is not found in the browser cache, the browser requests the operating system to search its cache for the required information.

4. **Resolver (ISP) Cache Lookup:**
   - In case the IP address is not located in the operating system cache, the browser consults the resolver, typically provided by the Internet Service Provider (ISP), to search its cache.

5. **Resolver Cache Lookup:**
   - If the IP address is still not found in the resolver's cache, the resolver initiates a request to a root server.

6. **Root Server Interaction:**
   - The root server plays a pivotal role by directing the resolver to the appropriate Top-Level Domain (TLD) server.

7. **TLD Server Interaction:**
   - The TLD server, having received the request, directs the resolver to the authoritative name servers responsible for the specific domain.

8. **Authoritative Name Server Interaction:**
   - The authoritative name server searches for the IP address associated with the requested domain and provides this information to the resolver.

9. **Resolver Caches IP Address:**
   - The resolver, upon obtaining the IP address, stores it in its cache to expedite future lookups and avoid redundancy.

10. **Resolver Provides IP to Browser:**
   - The resolver communicates the acquired IP address to the user's browser, enabling the browser to proceed with establishing a connection.

11. **Browser Sends Request to IP:**
   - The browser initiates a request to the obtained IP address, facilitating communication with the desired server.

12. **Wait for Response:**
   - The browser patiently awaits a response from the server, allowing time for the necessary data retrieval.

13. **Server Response:**
   - Finally, the server sends a response containing the requested data, which is then displayed to the user in the browser.

### Components
- **Server:** The physical or virtual machine where the web infrastructure is hosted.
- **Web Server (Nginx):** Handles incoming HTTP requests, serves static content, and directs requests to the application server.
- **Application Server:** Executes the web application code and processes dynamic content.
- **Application Files (Code Base):** The source code and files required for the web application.
- **Database (MySQL):** Stores and manages data for the web application.
- **Domain Name (foobar.com):** Configured with a www record (CNAME DNS type) pointing to the server's IP (8.8.8.8).

### Issues
1. **Single Point of Failure (SPOF):** This setup has a single server, making it vulnerable to failure. If the server goes down, the entire web application becomes inaccessible.
2. **Downtime during Maintenance:** Deploying new code or performing maintenance requires restarting the web server. During this time, the website may experience downtime.
3. **Limited Scalability:** Handling a sudden increase in incoming traffic can be challenging with a single server. Scaling horizontally (adding more servers) becomes necessary for better performance and reliability.

## [1. Distributed Web Infrastructure](https://github.com/MaryEhb/alx-system_engineering-devops/tree/main/0x09-web_infrastructure_design/1-distributed_web_infrastructure)

### Introduction
This repository contains the design for a two-server web infrastructure hosting www.foobar.com. It includes additional elements for improved scalability and redundancy.

### Components (In Addition to Simple Web Stack)
- **Server:** One additional server so that traffic between the two servers is distributed to improve redundancy.
- **Load Balancer (HAproxy):**
   - Purpose: Distributes incoming traffic among the web servers for load balancing.
   - Distribution Algorithm: Round Robin for simplicity and equal load distribution.

### Specifics:
- **Load Balancer Configuration:**
  - Round Robin Distribution: Distributes requests equally among servers in a circular order.

- **Active-Active vs. Active-Passive:**
  - Active-Active: Both servers actively handle requests simultaneously, improving performance.
  - Active-Passive: One server handles requests while the other is on standby, ready to take over if the active server fails.

- **Database Primary-Replica Cluster:**
  - Primary Node: Accepts write operations and replicates data to the replica nodes.
  - Replica Node: Read-only copy of the data, ensures fault tolerance and scalability.

- **Difference Between Primary and Replica:**
  - Primary Node: Handles write operations, and actively updates data.
  - Replica Node: Read-only, provides redundancy, and can take over in case the primary node fails.

### Issues
1. **Single Points of Failure (SPOF):** The Load Balancer is a potential SPOF. If it fails, traffic won't be distributed, leading to service disruption.
2. **Security Issues:**
   - No Firewall: Lack of a firewall exposes the servers to unauthorized access and potential security threats.
   - No HTTPS: Communication between clients and servers is not encrypted, making it vulnerable to interception and data manipulation.
3. **No Monitoring:** Lack of monitoring tools makes it challenging to identify and address performance issues, security breaches, or potential failures promptly.

## [2. Secured and Monitored Web Infrastructure](https://github.com/MaryEhb/alx-system_engineering-devops/tree/main/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure)

### Introduction
This repository outlines a two-server web infrastructure for www.foobar.com with enhanced security, encrypted traffic, and monitoring capabilities.

### Components (In Addition to Distributed Web Infrastructure)
- **3 Firewalls:**
  - Purpose: Added for enhanced security.
  - Control Network Traffic: Firewalls filter and monitor network traffic, preventing unauthorized access and potential security threats.
- **SSL Certificate:**
  - Purpose: Enables HTTPS to encrypt traffic during transmission, protecting it from eavesdropping and ensuring the integrity of the communication.
- **Monitoring Clients:**
  - Purpose: Installed to collect and analyze data for improved system health monitoring.

### Issues
1. **SSL Termination at Load Balancer:** Termination at the load balancer exposes decrypted traffic within the internal network, posing a security risk. Solution: Implement end-to-end encryption by terminating SSL at the web servers.
2. **Single MySQL Server for Writes:** Single point of failure for write operations on the MySQL server. Solution: Implement a MySQL Primary-Replica cluster to ensure fault tolerance and redundancy for write operations.
3. **Uniform Server Components:** Uniform components across servers pose a risk if a vulnerability is exploited. Solution: Implement diversity in server components or use a rolling update strategy to minimize the impact of vulnerabilities.

## [3. Scale Up](https://github.com/MaryEhb)

### Introduction

### Components (In Addition to Distributed Web Infrastructure)

### Issues
1. **Single Points of Failure (SPOF):** 
2. **Security Concerns:** 
3. **Monitoring QPS:** 
