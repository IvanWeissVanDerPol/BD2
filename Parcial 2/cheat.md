Here’s a **compact cheat sheet** summarizing the major topics you've covered on:

---

# ✅ **Databases Cheat Sheet**

---

## 1. **Transactions & Concurrency Control**

* **Transaction**: Unit of work; must be *atomic*.
* **ACID**:

  * **Atomicity**: All or nothing.
  * **Consistency**: Valid state transitions.
  * **Isolation**: Transactions don’t interfere.
  * **Durability**: Changes persist after commit.
* **2PL (Two-Phase Locking)**:

  * Growing (acquire locks) → Shrinking (release locks).
  * **Strict 2PL** holds X-locks until commit.
* **Deadlock Handling**:

  * **Detection**: Wait-for graph.
  * **Avoidance**: Timestamps (wait-die / wound-wait).
* **Serializability**:

  * **Conflict-serializable** ⇔ acyclic precedence graph.
  * **View-serializable**: Same reads/results as serial.
* **Distributed Locking**:

  * **Centralized**, **Primary Copy**, **Quorum**: $Q_r + Q_w > N, Q_w > N/2$

---

## 2. **Distributed Databases**

* **DDBS**: Logically unified, physically distributed DBs.
* **Transparency**:

  * *Location*, *Fragmentation*, *Replication*.
* **Fragmentation**:

  * *Horizontal*, *Vertical*, *Hybrid*.
* **Replication**:

  * *Full* vs *Partial*, *Synchronous* vs *Asynchronous*.
* **2PC Protocol**:

  * *Prepare* → *Commit/Abort*.
* **3PC Protocol**: Adds **Pre-commit**, avoids blocking.
* **Concurrency in DDB**:

  * Locking (Primary/Quorum), Timestamps, OCC.

---

## 3. **Data Warehousing & OLAP**

* **DW**: Subject-oriented, integrated, non-volatile, time-variant.
* **OLTP vs OLAP**:

  * OLTP → real-time, normalized; OLAP → historical, denormalized.
* **ETL**: Extract → Transform → Load.
* **OLAP Ops**: Roll-up, Drill-down, Slice, Dice, Pivot.
* **Schemas**:

  * *Star*: Fact + dimension (flat).
  * *Snowflake*: Normalized dimensions.
* **ROLAP/MOLAP/HOLAP**: Trade-offs between flexibility and speed.

---

## 4. **Big Data & NoSQL**

* **3 Vs**: Volume, Velocity, Variety.
* **Common Myths**:

  * Not just big size.
  * Complements SQL.
  * Not exclusive to large enterprises.
* **Tools**:

  * *Hadoop* (HDFS + MapReduce + YARN)
  * *Hive*, *Pig*, *Sqoop*, *Flume*
* **NoSQL Types**:

  * *Key-Value*: Redis
  * *Document*: MongoDB
  * *Column-Family*: Cassandra
  * *Graph*: Neo4j
* **Scalability**:

  * *Horizontal scaling* via sharding.
* **CAP Theorem**:

  * Can't have **Consistency**, **Availability**, and **Partition Tolerance** simultaneously.

---

## 5. **Data Modeling & Normalization**

* **ER → Relational**:

  * Entities → Tables
  * Relationships → FKs / Junction tables.
* **FD Types**:

  * *Full*, *Partial*, *Transitive*
* **Normal Forms**:

  * 1NF: Atomic values
  * 2NF: No partial dependencies
  * 3NF: No transitive dependencies
  * **BCNF**: LHS of every FD is a superkey

---

## 6. **SQL & Relational Algebra**

* **SQL Basics**:

  * `SELECT`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`
  * `INNER JOIN`, `LEFT JOIN`, `HAVING`
* **Window Functions**: `ROW_NUMBER()`, `RANK()`, `NTILE()`
* **CUBE / ROLLUP**: Aggregation extensions
* **Relational Algebra**:

  * `σ` (selection), `π` (projection), `⋈` (join), `∪`, `−`, `×`

---

Let me know if you’d like this exported to PDF, Notion, or formatted for Anki/Obsidian flashcards!
