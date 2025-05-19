# Transactions and Concurrency Control: Comprehensive Explanation

This document provides a comprehensive and deep explanation of the topic **"Transactions and Concurrency Control"** with structure, technical depth, examples, and coverage of centralized and distributed systems. The content is derived from standard academic and practical sources, such as *Fundamentos de Bases de Datos* and distributed systems literature.

---

## 1. Foundations: Transactions and Concurrency Control

### Core Concepts

#### Definition of a Transaction in DBMS

A **transaction** is a sequence of operations performed as a single logical unit of work. Each transaction must either be **fully completed** or **not executed at all**—ensuring data integrity.

**Example:**

Transferring $100 from Account A to B involves:

1. Read(A)
2. A := A - 100
3. Write(A)
4. Read(B)
5. B := B + 100
6. Write(B)

If this transaction fails after step 3, funds are lost unless rollback occurs.

#### ACID Properties

| Property        | Description                                                                                 | Example                                                                     |
| --------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Atomicity       | All operations in a transaction are treated as a single unit; either all happen or none do. | Bank transfer either fully completes or rolls back.                         |
| Consistency     | Ensures that the database moves from one valid state to another.                            | Integrity constraints remain valid (e.g., account balances ≥ 0).            |
| Isolation       | Concurrent transactions do not interfere with each other.                                   | Two people transferring money at the same time won't see inconsistent data. |
| Durability      | Once a transaction commits, its changes are permanent.                                      | System crash won't revert committed transactions.                           |

#### Lifecycle of a Transaction

1. **Begin**: Transaction is initiated.
2. **Read/Write**: Operations on data are performed.
3. **Validation**: Consistency check before commit.
4. **Commit**: Transaction successfully ends and changes persist.
5. **Abort**: On failure, rollback operations are applied.

#### Abstract Model of Transaction Systems

- **Centralized**:
  - Transactions are managed by a single DBMS.
  - All concurrency control and logging happen in a single place.
- **Distributed**:
  - Transactions span multiple nodes.
  - Use of coordinators, distributed commit protocols (like 2PC, 3PC).
  - Complexity arises from network delays and partial failures.

### Control Mechanisms

#### Concurrency Control Components in DBMS

1. **Scheduler**: Orders transaction operations.
2. **Lock Manager**: Grants and manages locks.
3. **Deadlock Manager**: Detects/resolves deadlocks.
4. **Recovery Manager**: Rolls back on failures.

#### Locking Protocols

- **Binary Locks**:
  - Two states: Locked (1) or Unlocked (0).
  - Simple but inflexible.
- **Shared/Exclusive Locks (S/X Locks)**:
  - Shared (S): Read-only; multiple can coexist.
  - Exclusive (X): Write access; must be alone.

| Operation | Required Lock |
| --------- | ------------- |
| Read      | Shared (S)    |
| Write     | Exclusive (X) |

- **Two-Phase Locking (2PL):**
  - **Basic 2PL**: Two phases:
    - Growing: Can acquire but not release locks.
    - Shrinking: Can release but not acquire new locks.
  - **Strict 2PL**: X-locks are held until commit/abort.
  - **Rigorous 2PL**: Both S and X locks held until the end.
  - Guarantees conflict-serializability.

#### Deadlock Handling

- **Detection (Wait-for Graph):**
  - Nodes: Transactions.
  - Edges: "Transaction A waits for B."
  - Cycle ⇒ Deadlock.
- **Avoidance:**
  - Use timestamps (e.g., wait-die, wound-wait protocols).
- **Prevention:**
  - Preallocate resources or disallow certain waits.
- **Starvation:**
  - Some transactions may never proceed.
  - Fairness mechanisms: priority queues, timeouts.

### Planning and Serializability

#### Scheduling and Conflict Serializability

- **Schedule**: Order of operations from multiple transactions.
- **Conflict Serializable**: If a schedule can be transformed (via swaps of non-conflicting ops) into a serial schedule.

#### Conflict vs. View Serializability

| Type         | Based On                | Complexity |
| ------------ | ----------------------- | ---------- |
| Conflict     | Conflicting operations  | Easier     |
| View         | Read-from relationships | Harder     |

#### Equivalence Classes of Schedules

Two schedules are **conflict equivalent** if:
- They involve the same operations and
- Conflicting ops are ordered the same.

#### Tests of Serializability

- **Precedence Graph (Serialization Graph):**
  - Nodes: Transactions
  - Edges: Order of conflicting ops
  - Acyclic ⇒ Conflict serializable

### Distributed Systems Specifics

#### Distributed Lock Management

1. **Centralized Lock Manager:**
   - Single site manages all locks.
   - Simple, but has a single point of failure and bottleneck risk.
2. **Primary Copy Protocol:**
   - Each data item has a primary site responsible for its locks.
   - Reduces load and improves locality.
3. **Majority-based Protocols:**
   - Transaction must get a majority of replicas to lock.
   - Increases fault-tolerance.
4. **Quorum Consensus Protocol:**
   - $Q_r$ = read quorum
   - $Q_w$ = write quorum
   - $N$ = total replicas
   - Condition:
     - $Q_r + Q_w > N$
     - $Q_w > N/2$
   - Example:
     - $N = 5$, $Q_r = 3$, $Q_w = 3$
     - Guarantees that at least one node will see all writes before any read.

---

## 2. Distributed Databases

### Architectural Understanding

#### Definition of a Distributed Database System

A **Distributed Database System (DDBS)** is a collection of multiple logically interrelated databases distributed over a computer network. Each site is managed by a local DBMS and participates in a global transaction system, enabling users to access data as if it were in a single centralized database.

**Key characteristics:**
- Data is physically distributed across nodes.
- Maintains logical transparency.
- Sites may be autonomous or tightly coupled.

#### Homogeneous vs. Heterogeneous Systems

| Aspect        | Homogeneous          | Heterogeneous                             |
| ------------- | -------------------- | ----------------------------------------- |
| Software      | Same DBMS            | Different DBMSs                           |
| Schema        | Shared global schema | Local schemas differ                      |
| Communication | Uniform protocol     | Wrappers or mediators needed              |
| Integration   | Easier               | Complex due to schema & model differences |

#### Data Transparency Types

Transparency refers to hiding complexity from users. Key types:

1. **Location Transparency**: Users query data without knowing its physical location.
2. **Fragmentation Transparency**: Users don't need to know how data is fragmented.
3. **Replication Transparency**: Users unaware of multiple copies (replicas) of the same data.

### Data Distribution Techniques

#### Data Fragmentation

- **Horizontal Fragmentation**: Rows are split based on predicates.
- **Vertical Fragmentation**: Columns are split while retaining primary key.
- **Hybrid Fragmentation**: Combination of horizontal and vertical.

#### Replication

- **Full Replication**: All data copied at every site.
- **Partial Replication**: Only a subset of data is replicated.
- **Synchronous Replication**: All replicas updated in real time (2PC often used).
- **Asynchronous Replication**: Updates sent to replicas after commit.

#### Allocation Strategies

Goal: Optimize performance, fault tolerance, and availability.

- **Centralized**: All data at one site.
- **Fragmented**: Only relevant fragments at each site.
- **Replicated**: Copies of critical data across sites.
- **Hybrid**: Combines above, tailored to usage patterns.

Factors considered:
- Access frequency
- Latency
- Update cost
- Site reliability

### Transaction Coordination

#### Two-Phase Commit Protocol (2PC / C2F)

Used to ensure atomicity across multiple sites.

- **Phase 1: Prepare**
  - Coordinator asks participants to prepare to commit.
  - Each participant writes to a log and replies with "ready" or "abort".
- **Phase 2: Commit/Abort**
  - If all say "ready", coordinator sends "commit".
  - Else, sends "abort".
  - Participants act accordingly.

#### Recovery from Failures

- **Participant failure**: Upon restart, consults log to determine if it should commit or abort.
- **Coordinator failure**: Participants wait; timeout and use termination protocols.

#### Three-Phase Commit Protocol (3PC)

Designed to avoid blocking (a flaw in 2PC).

- **CanCommit**: Coordinator asks if participants can commit.
- **PreCommit**: If all agree, a pre-commit message is sent.
- **DoCommit**: Final commit message sent.

Advantage: Non-blocking — participants can make decisions without coordinator in some failure scenarios.

### Concurrency in Distributed Systems

#### Locking-Based Strategies

1. **Primary Copy**: One site is authoritative for an item. Locking is delegated to this site.
2. **Quorum Protocol**: Read and write operations require subsets of replicas. Must satisfy:
   - $Q_r + Q_w > N$
   - $Q_w > N/2$
   - Ensures intersection between reads and writes.

#### Timestamp-Based Concurrency

- Each transaction assigned a timestamp.
- Operations respect timestamp order.
- If a conflict violates the order, transaction aborts.

**Example:**
- T1: timestamp 10, T2: timestamp 20
- T2 cannot overwrite data written by T1 if T1 hasn't committed yet.

#### Optimistic Concurrency Control (OCC)

- Transactions execute without locking.
- Validation occurs before commit.

**Phases:**
1. Read Phase: Read data and make changes locally.
2. Validation Phase: Check for conflicts.
3. Write Phase: Apply changes if no conflict.

Used in low-contention environments for higher performance.

---

## 3. Data Warehousing and OLAP

### Data Warehousing Concepts

#### What Is a Data Warehouse?

A **Data Warehouse (DW)** is a centralized repository used for analytical processing and decision-making, integrating data from multiple heterogeneous sources.

**Key Characteristics:**
- Subject-Oriented: Focuses on subjects (sales, customers).
- Integrated: Data from diverse sources is unified.
- Non-volatile: Once entered, data is rarely changed.
- Time-variant: Historical data is maintained.

#### Difference from OLTP

| Feature      | OLTP                           | Data Warehouse (OLAP)         |
| ------------ | ------------------------------ | ----------------------------- |
| Purpose      | Day-to-day operations          | Decision support & analytics  |
| Data         | Current, up-to-date            | Historical, aggregated        |
| Transactions | Short, frequent, insert/update | Long, complex, read-intensive |
| Schema       | Normalized (3NF)               | Denormalized (Star/Snowflake) |
| Speed        | Fast for writes                | Optimized for complex reads   |

#### ETL Process: Extract, Transform, Load

1. **Extract**: Gather data from source systems (e.g., relational DBs, flat files).
2. **Transform**: Cleanse, standardize, apply business rules (e.g., currency conversion).
3. **Load**: Move processed data into the DW.

Often done in batch jobs, and can involve incremental updates or full refreshes.

#### Snapshots & Time-Variant Data

- **Snapshots**: Capture the state of data at a point in time (e.g., monthly sales).
- **Time-variant data**: DW stores past values for trend analysis, forecasting.

### OLAP (Online Analytical Processing)

#### Multidimensional Analysis

OLAP enables analysis across multiple dimensions like time, geography, and product. Data is visualized as cubes, where each axis represents a dimension.

#### OLAP Operations

| Operation      | Description                                              |
| -------------- | -------------------------------------------------------- |
| Roll-up        | Aggregate data (e.g., from days to months).              |
| Drill-down     | Disaggregate (e.g., year → quarter → month).             |
| Slice          | Select a single dimension value (e.g., region = Europe). |
| Dice           | Select sub-cube with multiple dimension filters.         |
| Pivot          | Rotate cube to change perspective (rows ↔ columns).      |

### Modeling

#### Fact Tables vs. Dimension Tables

- **Fact Table**: Central table with measurable data (e.g., `sales_amount`, `units_sold`).
- **Dimension Table**: Contains attributes for filtering and grouping (e.g., `time`, `product`, `store`).

#### Star Schema

- Fact table at center.
- Dimension tables connected directly.
- Denormalized, simpler joins, faster queries.

#### Snowflake Schema

- Dimensions normalized into multiple related tables.
- More complex joins, but better data integrity and storage optimization.

**Example:**

| Fact Table  | Dimensions           |
| ----------- | -------------------- |
| Sales_Fact  | Date, Product, Store |
| Measures    | Quantity, Revenue    |

### OLAP Architectures

| Architecture                      | Description                                                                                   |
| --------------------------------- | --------------------------------------------------------------------------------------------- |
| ROLAP (Relational OLAP)           | Uses relational DBMS for data storage. Supports large volumes and complex queries.            |
| MOLAP (Multidimensional OLAP)     | Uses specialized multidimensional databases (MDDB). Fast for cube operations.                 |
| HOLAP (Hybrid OLAP)               | Combines both: stores summary in MDDB, detail in RDBMS. Balances performance and scalability. |

---

## 4. Big Data and NoSQL

### Big Data Fundamentals

#### What Is Big Data?

**Big Data** refers to datasets that are too large, fast-changing, or complex to be managed with traditional data processing tools. It's not just about size—it's about the challenges in storage, processing, and analysis.

#### The 3 V's of Big Data

| V            | Description                                                                             |
| ------------ | --------------------------------------------------------------------------------------- |
| Volume       | Scale of data (terabytes to petabytes).                                                 |
| Velocity     | Speed at which data is generated, ingested, and processed (real-time, near-real-time).  |
| Variety      | Different forms of data: structured, semi-structured, unstructured (text, logs, video). |

#### Common Misconceptions

- Myth: Big Data = just large data → Reality: It's more about complexity and processing needs.
- Myth: Big Data replaces all traditional databases → Reality: They complement each other.
- Myth: Big Data always means NoSQL → Reality: Some Big Data tools use SQL-based interfaces (e.g., Hive).

### Ecosystem and Tools

#### Hadoop Architecture

A distributed computing framework for Big Data processing.

- **HDFS (Hadoop Distributed File System):**
  - Stores large files across multiple nodes.
  - Fault-tolerant and high-throughput.
- **MapReduce:**
  - Programming model for batch processing.
  - Map: Filters and sorts data.
  - Reduce: Aggregates results.
- **YARN (Yet Another Resource Negotiator):**
  - Resource management and job scheduling.

#### Higher-Level Tools

| Tool      | Function                                                         |
| --------- | ---------------------------------------------------------------- |
| Hive      | SQL-like querying on Hadoop.                                     |
| Pig       | Scripting language for transformation tasks.                     |
| Sqoop     | Transfers data between Hadoop and RDBMS.                         |
| Flume     | Collects, aggregates, and moves large volumes of streaming logs. |

#### Data Pipelines & Real-Time Challenges

- Big Data systems handle batch and real-time workloads.
- Challenges:
  - Data ingestion at scale.
  - Low latency requirements.
  - Fault tolerance.
  - Example tools: Apache Kafka (streaming), Apache NiFi (flow automation).

### NoSQL Databases

#### Definition and Motivation

- NoSQL = "Not only SQL". Designed for:
  - Scalability (horizontal/cluster-based).
  - Schema flexibility.
  - High availability and fault tolerance.
  - Handling semi-structured or unstructured data.

#### Types of NoSQL Databases

| Type                    | Description                                                  | Examples         |
| ----------------------- | ------------------------------------------------------------ | ---------------- |
| Key-Value Store         | Simple pair of key and value. Optimized for fast access.     | Redis, DynamoDB  |
| Document Store          | Stores JSON/XML-like documents with rich structure.          | MongoDB, CouchDB |
| Column-Family Store     | Tables with flexible column groupings. Optimized for writes. | Cassandra, HBase |
| Graph Database          | Stores entities and relationships as graphs.                 | Neo4j, ArangoDB  |

### Scalability Models

#### Horizontal Scaling (Sharding)

- Sharding: Distributes data across multiple nodes.
- Allows scale-out by adding commodity servers.
- Each shard contains a subset of the data.

**Example:**

```text
Customer_ID 1–1000 → Shard A
Customer_ID 1001–2000 → Shard B
```

#### CAP Theorem

States that a distributed system cannot simultaneously guarantee all three:

| Property                    | Definition                                             |
| --------------------------- | ------------------------------------------------------ |
| Consistency (C)             | All nodes see the same data at the same time.          |
| Availability (A)            | Every request gets a (non-error) response.             |
| Partition Tolerance (P)     | System continues to function despite network failures. |

Implication: Must choose two out of three (e.g., CA, CP, or AP systems).

---

## 5. Data Modeling and Normalization

### Entity-Relationship (ER) Modeling

#### Basic Concepts

- **Entity**: A real-world object or concept (e.g., Student, Course).
- **Attribute**: Property of an entity (e.g., StudentID, Name).
- **Relationship**: Association between entities (e.g., Enrolled connects Student and Course).

#### Participation & Cardinality

| Concept           | Description                                                                               |
| ----------------- | ----------------------------------------------------------------------------------------- |
| Participation     | Total: every instance must participate. <br> Partial: some instances participate.         |
| Cardinality       | Expresses the number of related entities: 1:1, 1:N, N:M.                                 |
| Example           |                                                                                           |

```text
STUDENT (StudentID, Name)
COURSE (CourseID, Title)
ENROLLED (StudentID, CourseID, Grade)
```

Here, ENROLLED is a many-to-many relationship (N:M).

### Transforming ER to Relational Model

#### Mapping Rules

1. **Entity → Table**:
   - Each entity becomes a relation.
   - Attributes become columns.
   - Primary key chosen.
2. **Relationship → Foreign Keys**:
   - Binary 1:N → add FK in N side.
   - Binary N:M → create junction table with FKs from both sides.
   - 1:1 → FK added to either side depending on participation.

**Example:**

```text
STUDENT(StudentID PK, Name)
COURSE(CourseID PK, Title)
ENROLLED(StudentID FK, CourseID FK, Grade)
```

### Functional Dependencies (FDs)

#### Definition

A **functional dependency** X → Y holds if two tuples with the same value for X also agree on Y.

#### Types of FDs

| Type           | Description                                 |
| -------------- | ------------------------------------------- |
| Full           | Y depends on all of X.                      |
| Partial        | Y depends on part of a composite key.       |
| Transitive     | X → Y and Y → Z implies X → Z (transitive). |

**Example:**

```text
StudentID → Name       (Full)
(StudentID, CourseID) → Grade  (Full)
CourseID → DepartmentID → DepartmentName (Transitive)
```

### Normal Forms

Normalization is the process of removing redundancy and ensuring data integrity through decomposition based on functional dependencies.

#### 1NF – First Normal Form

- No repeating groups.
- Atomic values only.

**Violation:**

```text
StudentID | Name | Courses
-----------------------------
1         | Alice| Math, CS  ← repeating group
```

#### 2NF – Second Normal Form

- In 1NF and
- No partial dependencies (i.e., non-key attribute depends on part of a composite key).

**Violation:**

```text
(StudentID, CourseID) → Grade
StudentID → Name  ← partial dependency
```

**Solution:**
Split into:
- STUDENT(StudentID, Name)
- ENROLLMENT(StudentID, CourseID, Grade)

#### 3NF – Third Normal Form

- In 2NF and
- No transitive dependencies (non-key → non-key → attribute).

**Violation:**

```text
CourseID → DepartmentID
DepartmentID → DepartmentName
```

**Solution:**
Split into:
- COURSE(CourseID, DepartmentID)
- DEPARTMENT(DepartmentID, DepartmentName)

#### Boyce-Codd Normal Form (BCNF)

- A stronger version of 3NF.
- For every functional dependency X → Y, X must be a superkey.

**When 3NF is not enough:**

```text
FDs: A → B, B → A (but neither is a superkey)
```

BCNF requires decomposition of such tables even if they are in 3NF.

#### Decomposition and Lossless Joins

When decomposing:
- Ensure lossless join (can reconstruct original table from parts).
- Ensure dependency preservation (don't lose FDs).

**Lossless Join Test (simple case):**
If R is decomposed into R1 and R2:
- If R1 ∩ R2 → R1 or R2, then join is lossless.

---

## 6. SQL and Relational Algebra

### Basic SQL Queries

#### Core Clauses

1. **SELECT**: Retrieves specific columns.
   - `SELECT name, age FROM employees;`
2. **WHERE**: Filters rows.
   - `SELECT * FROM employees WHERE age > 30;`
3. **JOINs**: Combines rows from two tables based on a condition.

| Type           | Description                              | Example                                 |
| -------------- | ---------------------------------------- | --------------------------------------- |
| INNER JOIN     | Only matching rows from both tables.     | ...FROM A INNER JOIN B ON A.id = B.id   |
| LEFT JOIN      | All rows from left, matching from right. | ...FROM A LEFT JOIN B ON A.id = B.id    |

4. **GROUP BY**: Groups rows for aggregation.
   - `SELECT department, COUNT(*) FROM employees GROUP BY department;`
5. **HAVING**: Filters after grouping.
   - `...GROUP BY dept HAVING COUNT(*) > 10;`
6. **ORDER BY**: Sorts output.
   - `...ORDER BY salary DESC;`
7. **Aggregations**: `COUNT()`, `SUM()`, `AVG()`, `MAX()`, `MIN()`

### Advanced SQL

#### Window Functions

These operate over partitions of the result set, useful for ranking and analysis.

| Function       | Description                    |
| -------------- | ------------------------------ |
| ROW_NUMBER()   | Unique row ID within partition |
| RANK()         | Ranking with gaps for ties     |
| DENSE_RANK()   | No gaps in ranking             |
| NTILE(n)       | Divides rows into n buckets    |

**Example:**

```sql
SELECT name, salary,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

#### CUBE and ROLLUP

Extensions to GROUP BY for multi-dimensional analysis.

- **ROLLUP**: Hierarchical subtotaling.

  ```sql
  SELECT department, role, SUM(salary)
  FROM employees
  GROUP BY ROLLUP(department, role);
  ```

  Generates totals per role, per department, and grand total.

- **CUBE**: All combinations of aggregations.

  ```sql
  SELECT department, role, SUM(salary)
  FROM employees
  GROUP BY CUBE(department, role);
  ```

### Relational Algebra

Mathematical language for querying relational data.

#### Basic Operations

| Operation             | Symbol | SQL Equivalent  |
| --------------------- | ------ | --------------- |
| Selection             | σ      | WHERE clause    |
| Projection            | π      | SELECT clause   |
| Union                 | ∪      | UNION           |
| Difference            | −      | EXCEPT          |
| Cartesian Product     | ×      | FROM A, B       |
| Join                  | ⋈      | JOIN ON         |

#### Examples

- **Selection (σ):**

  ```text
  σ_age > 30 (Employees)
  → SELECT * FROM Employees WHERE age > 30;
  ```

- **Projection (π):**

  ```text
  π_name, age (Employees)
  → SELECT name, age FROM Employees;
  ```

- **Join (⋈):**

  ```text
  Employees ⋈_Employees.dept_id = Departments.id Departments
  → SELECT * FROM Employees JOIN Departments ON Employees.dept_id = Departments.id;
  ```

### Translating SQL to Relational Algebra

**SQL:**

```sql
SELECT e.name
FROM Employees e JOIN Departments d ON e.dept_id = d.id
WHERE d.name = 'Sales';
```

**Relational Algebra:**

```text
π_e.name (σ_d.name = 'Sales' (Employees ⋈_e.dept_id = d.id Departments))
``` 