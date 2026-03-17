# Routing Pattern

The Routing Pattern is a pattern in which a coordinator agent analyzes a user’s request and routes it to the most
appropriate specialized agent for execution.

This pattern is useful when:

* **Making dynamic decisions**. Allows the system to choose the most appropriate action based on the current context or user input.
* **Navigating across different scenarios**. Enables smooth handling of multiple possible workflows or situations without hardcoding each path.
* **Promoting loose coupling**. Reduces dependencies between components, making them easier to modify, replace, or test independently.
* **Ensuring separation of concerns**. Keeps responsibilities clearly divided, so each component focuses on a single task, improving maintainability and clarity.

## Running the scripts

### Travel Concierge

Travel Concierge is a specialized service that coordinates the discovery, selection, and booking of travel options,
including air logistic, accommodation, experiences and culture, documentation and visa, and finance and budget.

To run the **Google ADK** script, execute the following command:

```shell
python routing_adk.py
```

#### Air Logistic Agent

Inquiry:
```markdown
What are the best airlines flying from Mexico City to Las Vegas?
```

Possible output:
```markdown
The coordinator has resolved the user's inquiry: The best airlines flying from Mexico City to Las Vegas are:
*   Aeromexico
*   Volaris
*   VivaAerobus
```

#### Accommodation Agent

Inquiry:
```markdown
List three hotels near the Sphere in Las Vegas.
```

Possible output:
```markdown
The coordinator has resolved the user's inquiry: The following are three hotels near the Sphere in Las Vegas:

1. The Venetian Resort Las Vegas
2. The Palazzo at The Venetian Resort
3. MGM Grand Hotel & Casino
```

#### Experiences & Culture Agent

Inquiry:
```markdown
What unique experiences can I do in Edinburgh in three days?
```

Possible output:
```markdown
The coordinator has resolved the user's inquiry: I can help you with that! Edinburgh is a city rich in history and culture, offering a variety of unique experiences. Here are a few ideas for a three-day itinerary:

**Day 1: Royal Mile & Historic Heart**

*   **Morning:** Start at the top of the Royal Mile with a visit to **Edinburgh Castle**. Allow at least 2-3 hours to explore its ramparts, Crown Jewels, and the Great Hall.
*   **Lunch:** Grab a traditional Scottish lunch at a pub along the Royal Mile.
*   **Afternoon:** Wander down the Royal Mile, exploring its closes (narrow alleyways) and historic closes like Mary King's Close for a glimpse into the city's hidden past. Visit **St Giles' Cathedral**.
*   **Evening:** Enjoy a traditional Scottish music session at a pub in the Grassmarket area, or consider a spooky **ghost tour** that delves into Edinburgh's darker history.

**Day 2: Arthur's Seat, Holyrood & Calton Hill**

*   **Morning:** Hike up **Arthur's Seat**, an ancient volcano in Holyrood Park, for panoramic views of the city. It's a relatively easy hike and very rewarding.
*   **Lunch:** Have a picnic in Holyrood Park or find a cafe nearby.
*   **Afternoon:** Visit the **Palace of Holyroodhouse**, the King's official residence in Scotland, and explore its State Apartments and historic ruins.
*   **Late Afternoon:** Climb **Calton Hill** for iconic views of the city, including the National Monument and Dugald Stewart Monument.
*   **Evening:** Experience a **whisky tasting** at a specialized bar, learning about Scotland's national drink.

**Day 3: Museums, Culture & Leith**

*   **Morning:** Immerse yourself in art at the **Scottish National Gallery** or explore the **National Museum of Scotland** for a diverse range of exhibits, from natural history to technology and Scottish heritage.
*   **Lunch:** Enjoy lunch in the museum cafe or in the city center.
*   **Afternoon:** Take a trip to **Leith**, Edinburgh's vibrant port district. Visit the **Royal Yacht Britannia** and explore the trendy shops and cafes along the waterfront.
*   **Evening:** Enjoy a farewell dinner in Leith, known for its excellent seafood restaurants.

**Unique Experiences to Consider:**

*   **Camera Obscura and World of Illusions:** A fun and interactive experience with optical illusions and stunning city views from its tower.
*   **Scotch Whisky Experience:** A more in-depth tour and tasting focused on the different types of Scotch whisky.
*   ** a traditional Scottish Ceilidh:** If you're lucky to be there on a night with a public ceilidh, it's a fantastic way to experience Scottish folk dancing and music.
*   **Explore the Dean Village:** A picturesque oasis on the Water of Leith, offering a tranquil escape from the city bustle.

Remember to book popular attractions like Edinburgh Castle in advance, especially during peak season! Enjoy your trip to Edinburgh!
```

#### Documentation & Visa Agent

Inquiry:
```markdown
Do Mexican citizens need a visa to travel to the United States?
```

Possible output:
```markdown
The coordinator has resolved the user's inquiry: Do Mexican citizens need a visa to travel to the United States?
This depends on the purpose and duration of their stay. Generally, Mexican citizens traveling to the U.S. for tourism, business, or study may need a visa, such as a B-1/B-2 visa for short stays or an F-1 visa for students. However, there are exceptions, like the Visa Waiver Program (VWP), which allows citizens of certain countries to travel to the U.S. for tourism or business for stays of 90 days or less without obtaining a visa. Mexico is not part of the VWP. Therefore, most Mexican citizens will require a visa to enter the U.S. It is always recommended to check the official website of the U.S. Department of State or the U.S. embassy or consulate in Mexico for the most up-to-date and specific information regarding visa requirements.
```

#### Finance & Budget Agent

Inquiry:
```markdown
Convert the total trip cost from USD to MXN. $10,000 USD.
```

Possible output:
```markdown
The coordinator has resolved the user's inquiry: The total trip cost is $10,000 USD, which is equivalent to 170,000 Mexican Pesos (MXN).
```
