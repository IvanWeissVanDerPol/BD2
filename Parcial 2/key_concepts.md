# 🧠 1. Foundations: Transactions and Concurrency Control

## 🔹 Core Concepts
- Definition of a Transaction in DBMS
- ACID properties (Atomicity, Consistency, Isolation, Durability)
- Lifecycle of a Transaction
- Abstract model of a transaction system (centralized and distributed)

## 🔹 Control Mechanisms
- Concurrency Control components in DBMS
- Locking protocols:
  - Binary Locks
  - Shared/Exclusive (S/X) Locks
  - Two-Phase Locking (2PL):
    - Basic 2PL
    - Strict 2PL
    - Rigorous 2PL
- Deadlock handling:
  - Detection (Wait-for Graph)
  - Avoidance and prevention
  - Starvation and fairness

## 🔹 Planning and Serializability
- Scheduling and conflict serializability
- Conflict vs. View Serializability
- Equivalence classes of schedules
- Definitions and tests of serializability

## 🔹 Distributed Systems Specifics
- Distributed Lock Management:
  - Centralized lock manager
  - Primary Copy
  - Majority-based protocols
  - Quorum Consensus Protocol (Q<sub>r</sub> + Q<sub>w</sub> > N)

📚 Source: Libro Fundamentos de Bases de Datos (Cap. 18-19, 22) and 8 Bases de Datos Distribuidas.ppt

# 🌍 2. Distributed Databases

## 🔹 Architectural Understanding
- Definition of a Distributed Database System
- Homogeneous vs. Heterogeneous systems
- Data transparency types:
  - Location transparency
  - Fragmentation transparency
  - Replication transparency

## 🔹 Data Distribution Techniques
- Data Fragmentation:
  - Horizontal
  - Vertical
  - Hybrid
- Replication:
  - Full, partial
  - Synchronous vs asynchronous replication
- Allocation Strategies for performance and fault tolerance

## 🔹 Transaction Coordination
- Two-Phase Commit Protocol (2PC / C2F):
  - Phase 1: Prepare
  - Phase 2: Commit/Abort
  - Recovery from participant/coordinator failures
- Three-Phase Commit (3PC): fail-safe coordination

## 🔹 Concurrency in Distributed Systems
- Distributed concurrency control strategies:
  - Locking-based (quorum, primary copy)
  - Timestamp-based
  - Optimistic concurrency

📚 Source: Libro Fundamentos de Bases de Datos (Cap. 19) and 8 Bases de Datos Distribuidas.ppt

# 🧊 3. Data Warehousing and OLAP

## 🔹 Data Warehousing Concepts
- Definition and purpose of a Data Warehouse (DW)
- Differences from OLTP systems
- ETL process: Extract, Transform, Load
- Snapshots and time-variant data

## 🔹 OLAP (Online Analytical Processing)
- Multidimensional analysis concepts
- OLAP operations:
  - Roll-up / Drill-down
  - Slice and Dice
  - Pivot
- Cubes and dimensional modeling

## 🔹 Modeling
- Fact tables and dimension tables
- Star schema vs Snowflake schema
- Examples of facts (sales, revenue) and dimensions (time, store, product)

## 🔹 OLAP Architectures
- ROLAP (Relational OLAP)
- MOLAP (Multidimensional OLAP)
- HOLAP (Hybrid OLAP)

📚 Source: 9 DATAWAREHOUSE.pptx and Libro Fundamentos de Bases de Datos Cap. 22

# 🌐 4. Big Data and NoSQL

## 🔹 Big Data Fundamentals
- What Big Data is and isn't
- 3 V's:
  - Volume
  - Velocity
  - Variety
- Common misconceptions about Big Data

## 🔹 Ecosystem and Tools
- Hadoop Architecture
- HDFS
- MapReduce
- Hive, Pig, Sqoop, Flume
- Data pipelines and real-time ingestion challenges

## 🔹 NoSQL Databases
- Definition and motivation (schema flexibility, scalability)
- Types of NoSQL:
  - Key-Value Stores (Redis, DynamoDB)
  - Document Stores (MongoDB, CouchDB)
  - Column-Family Stores (Cassandra, HBase)
  - Graph Databases (Neo4j)

## 🔹 Scalability Models
- Horizontal scaling (Sharding)
- CAP theorem (Consistency, Availability, Partition Tolerance)

📚 Source: 10 NoSQL.pptx and 11 Big Data.pptx

# 🧩 5. Data Modeling and Normalization

## 🔹 Entity-Relationship (ER) Modeling
- Entities, attributes, relationships
- Participation (total/partial), cardinality (1:N, N:M)

## 🔹 Transforming ER to Relational Model
- Mapping rules: entities → tables, relationships → foreign keys

## 🔹 Functional Dependencies
- Determining dependencies from relations
- Full, partial, and transitive dependencies

## 🔹 Normal Forms
- 1NF, 2NF, 3NF
- Boyce-Codd Normal Form (BCNF)
- Decomposition and lossless joins

📚 You'll need a foundational DB textbook or slides—this content is not in the uploaded files but commonly precedes the provided material in course structure.

# 🧮 6. SQL and Relational Algebra

## 🔹 Basic SQL Queries
- SELECT, WHERE, JOIN, GROUP BY, ORDER BY
- LEFT JOIN, INNER JOIN, COUNT, SUM, HAVING

## 🔹 Advanced SQL
- Window functions: RANK(), ROW_NUMBER(), NTILE()
- CUBE and ROLLUP in aggregations (OLAP extensions)

## 🔹 Relational Algebra
- Basic operations: Selection, Projection, Join, Union, Difference
- Expressing SQL queries as algebra expressions

📚 Partially covered in Libro Fundamentos de Bases de Datos (Cap. 22)
