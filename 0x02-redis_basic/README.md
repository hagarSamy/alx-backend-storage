REDIS
## Redis (Remote Dictionary Server) is
- an open-source,
- in-memory data structure store
that can be used as a database, cache, message broker, and queue. It's known for its exceptional performance and versatility.

## Key Features
    - In-memory data storage for high-speed operations
    - Support for various data structures (strings, hashes, lists, sets, sorted sets)
    - Built-in replication and different levels of on-disk persistence
    - Transactions and Pub/Sub messaging paradigm
    - Lua scripting capabilities

## Use Cases

Redis is widely used in various scenarios, including:

- Caching to improve application performance
- Real-time analytics and counting
- Session management in web applications
- Leaderboards and counting in gaming applications
- Queues for background job processing

## Data Structures

Redis supports several data structures, making it versatile for different use cases:

- Strings: Binary-safe strings up to 512MB in size
- Lists: Collections of string elements sorted by insertion order
- Sets: Unordered collections of unique strings
- Sorted Sets: Similar to sets but with an associated score for sorting
- Hashes: Maps between string fields and string values

## Performance

Redis is known for its high performance due to its in-memory nature and efficient data structures. It can handle millions of requests per second, making it suitable for high-load, real-time applications.

## Persistence

While Redis is an in-memory database, it offers persistence options:

data store, which means it keeps its entire dataset in RAM. This approach allows for extremely fast read and write operations, as accessing data from memory -- much quicker than retrieving it from disk. However, to ensure data durability and prevent data loss in case of system failures,

- RDB (Redis Database): Point-in-time snapshots at specified intervals
- AOF (Append Only File): Logs every write operation for rebuild on restart
- Hybrid approach combining both RDB and AOF
