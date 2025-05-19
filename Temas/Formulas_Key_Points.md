# Database Formulas and Key Points for Exams

## 1. Index Performance Formulas

### Search Time Complexity
- Linear Search: O(n)
- Binary Search: O(log n)
- Hash Search: O(1) average, O(n) worst case
- B+ Tree Search: O(log n)

### Index Space Overhead
- Dense Index: n entries
- Sparse Index: n/B entries (where B is block size)
- B+ Tree: O(n/B) pages

## 2. Disk Performance Formulas

### Access Time
```
Total Access Time = Seek Time + Rotational Latency + Transfer Time
```
### Rotational Latency
```
Average Rotational Latency = (1/2) × (1/RPM) × 60 seconds
```
### Transfer Time
```
Transfer Time = (Number of Bytes) / (Transfer Rate)
```
### Disk I/O Cost
```
I/O Cost = Number of Block Accesses × (Seek Time + Rotational Latency + Transfer Time)
```
## 3. RAID Storage Formulas

### RAID 0 (Striping)
- Storage Efficiency: 100%
- Read Performance: n × Single Disk Speed
- Write Performance: n × Single Disk Speed
- Fault Tolerance: None

### RAID 1 (Mirroring)
- Storage Efficiency: 50%
- Read Performance: n × Single Disk Speed
- Write Performance: 1 × Single Disk Speed
- Fault Tolerance: n-1 disks

### RAID 5
- Storage Efficiency: (n-1)/n
- Read Performance: n × Single Disk Speed
- Write Performance: 1/4 × Single Disk Speed
- Fault Tolerance: 1 disk

## 4. B+ Tree Formulas

### Node Size
```
Maximum Keys = Block Size / (Key Size + Pointer Size)
```
### Height
```
Maximum Height = log⌈m/2⌉((n+1)/2)
```
where:
- m is the order of the B+ tree
- n is the number of keys

### Space Utilization
```
Minimum Space Utilization = 50%
```
## 5. Query Processing Formulas

### Join Cost
```
Nested Loop Join Cost = |R| + |R| × |S|
```
where:
- |R| is the size of relation R
- |S| is the size of relation S

### Selection Cost
```
Linear Scan Cost = |R|
Index Scan Cost = Height of Index + Number of Matching Records
```
## Key Points to Memorize

### 1. Index Fundamentals
- Indexes trade space for speed
- Primary vs Secondary indexes
- Dense vs Sparse indexes
- Clustered vs Unclustered indexes

### 2. File Organization
- Heap: O(1) insert, O(n) search
- Sequential: O(log n) search, O(n) insert
- Hash: O(1) average search, O(n) worst case
- Clustered: Better for range queries

### 3. Disk Performance
- Seek time is the largest component of access time
- Buffer management reduces I/O
- Elevator algorithm minimizes head movement
- Block size affects I/O efficiency

### 4. RAID Levels
- RAID 0: Performance, no redundancy
- RAID 1: Mirroring, high reliability
- RAID 5: Balance of performance and reliability
- RAID 10: Best performance and reliability

### 5. B+ Trees
- All data in leaves
- Balanced height
- Multiple keys per node
- Linked leaves for range queries

### 6. Search Algorithms
- Linear: Simple but slow
- Binary: Fast but requires sorted data
- Hash: Fastest but no range queries
- B+ Tree: Good for both point and range queries

### 7. Query Processing
- Parsing → Optimization → Execution
- Cost-based optimization
- Materialization vs Pipelining
- Join algorithms and their costs

### 8. ACID Properties
- Atomicity: All or nothing
- Consistency: Valid state
- Isolation: No interference
- Durability: Permanent changes

## Exam Tips
1. Remember the trade-offs between different approaches
2. Understand when to use each type of index
3. Know the formulas for calculating costs
4. Be able to explain real-world examples
5. Understand the relationships between concepts
6. Practice drawing diagrams (especially for B+ trees)
7. Know the advantages and disadvantages of each approach
8. Be able to compare different solutions
9. Understand the impact of different parameters
10. Remember the key formulas and their components

## Common Exam Questions
1. Compare and contrast different index types
2. Calculate disk access times
3. Analyze RAID configurations
4. Draw and manipulate B+ trees
5. Calculate query processing costs
6. Explain ACID properties with examples
7. Compare different file organizations
8. Analyze search algorithm performance
9. Explain optimization techniques
10. Discuss trade-offs in database design 
