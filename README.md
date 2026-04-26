Reflection
How do you write programs that are maintainable, readable, and adaptable?

To write maintainable, readable, and adaptable programs, I focus on organizing code into clear, reusable components and using consistent naming conventions. 
In this project, I created a separate CRUD Python module to handle all database interactions. 
This made the code easier to manage because the dashboard logic and database logic were not mixed together. 
If something needed to be changed, such as how data is retrieved or updated, I could modify the CRUD module without affecting the dashboard layout.

The advantage of working this way is that it improves scalability and reusability.
The CRUD module can be reused in future projects that require database access, even if the front-end interface is different.
In the future, I could use this same module for other dashboards, web applications, or data analysis tools that interact with MongoDB, 
which saves time and promotes consistency across projects.

How do you approach a problem as a computer scientist?
When approaching a problem, I start by breaking it down into smaller, manageable parts and identifying the key requirements. 
For this project, I focused first on understanding the database structure and the types of queries needed to support the dashboard filters. 
Then, I built the backend functionality before connecting it to the front-end components.

This approach was different from previous assignments because it required integrating multiple technologies, 
including Python, MongoDB, and Dash, rather than working on isolated problems. 
I had to think more about how each part of the system interacts with the others. In the future, I would continue using this structured approach by clearly 
defining requirements, designing the data model first, and then building modular components that can be tested independently before integration.

What do computer scientists do, and why does it matter?

Computer scientists design and build systems that solve real-world problems by organizing, processing, and presenting data in meaningful ways. 
Their work matters because it helps organizations make informed decisions and operate more efficiently.

In this project, the dashboard allows Grazioso Salvare to filter and analyze animal rescue data quickly and visually. 
Instead of manually reviewing large datasets, users can interact with the dashboard to identify patterns, track specific rescue categories, and view geographic data. 
This improves decision-making, saves time, and increases overall productivity. Projects like this demonstrate how technology can turn raw data into actionable insights 
that directly support an organization’s goals.
