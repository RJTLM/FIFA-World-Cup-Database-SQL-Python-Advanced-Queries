# Database Design and Implementation Report

## Cover Page

### Final Assessment: Database System for FIFA Women's World Cup
#### Student Name: Ryan Mackintosh
#### Student ID: 21171466
#### Lab Group: Thursday 8am

## Table of Contents

- [Introduction](#introduction)
- [Design of the Database](#design-of-the-database)
  - [Entity Selection](#entity-selection)
  - [ER Diagram](#er-diagram)
  - [Relational Schema](#relational-schema)
  - [Data Description](#data-description)
  - [Assumptions](#assumptions)
- [Implementation of the Database and Adding Sample Data](#implementation-of-the-database-and-adding-sample-data)
  - [Database Implementation](#database-implementation)
  - [Sample Data and Insertion](#sample-data-and-insertion)
- [Use of the Database](#use-of-the-database)
  - [Queries](#queries)
  - [Advanced Features](#advanced-features)
  - [Database Connectivity and Python Implementation](#database-connectivity-and-python-implementation)
- [Discussion](#discussion)
- [References](#references)

## Introduction

_Brief overview of the work done, the selected scenario, and activities undertaken._

## Design of the Database

### Entity Selection

_Explanation of the selected entities, relationships, data types, etc._
##### Entity Sets, Relationship Sets, and Cardinality Constraints

**Entity Set**
| Entity Set   | Key         | Other Attributes                                                                                      | Relationship Set | Between Entity Sets | Attributes | Relationship Set Cardinality | Participation / Other Constraints                      |
|--------------|-------------|-------------------------------------------------------------------------------------------------------|------------------|---------------------|------------|-----------------------------|--------------------------------------------------------|
| Match        | MatchID     | home_score, away_score, home_penalty, away_penalty, Attendance, Venue, Round, MatchDate, Notes, MatchHost | Is Played In     | Match-Event         | EventID    | Many-One                    | Each Match is associated with one Event; An Event can have multiple Matches |
| Team         | TeamName    |                                                                                                       | Plays            | Match-Team          | MatchID, HomeAway | Many-Many                | A Team can play in many Matches; A Match involves two Teams |
| Player       | PlayerName  | isCaptain                                                                                             |                  |                     |            |                             |                                                          |
| Event        | EventID     | EventYear, EventHost, NoTeams, Champion, RunnerUp, TopScorer, EventAttendance, EventAttendanceAvg, NoMatches | Is Played In     | Match-Event         | MatchID    | Many-One                    | Each Match is associated with one Event; An Event can have multiple Matches |
| Manager      | ManagerName |                                                                                                       | Manages          | Match-Manager       | MatchID    | Many-Many                    | A Manager can manage in many Matches; A Match can have multiple Managers |
| Referee      | RefereeName |                                                                                                       | Officiates       | Match-Referee       | MatchID    | Many-One                    | A Referee can officiate many Matches; A Match is officiated by one Referee |

**Relationship Set**
| Relationship Set | Between Entity Sets | Attributes | Relationship Set Cardinality | Participation / Other Constraints |
|------------------|---------------------|------------|-----------------------------|--------------------------------------------------------|
| Plays            | Match-Team          | MatchID, TeamName, HomeAway | Many-Many                | A Team can play in many Matches; A Match involves two Teams |
| Manages          | Match-Manager       | MatchID, ManagerName | Many-Many                    | A Manager can manage in many Matches; A Match can have multiple Managers |
| Officiates       | Match-Referee       | MatchID, RefereeName | Many-One                    | A Referee can officiate many Matches; A Match is officiated by one Referee |
| Is Played In     | Match-Event         | MatchID, EventID | Many-One                    | Each Match is associated with one Event; An Event can have multiple Matches |

### ER Diagram

_Inclusion of the ER diagram visualizing the structure of the database._

### Relational Schema

_Presentation of the relational schema with tables, attributes, and relationships._

### Data Description

_Description of the data and its organization within the database._

### Assumptions

_Any assumptions made during the design of the database._

## Implementation of the Database and Adding Sample Data

### Database Implementation

_Description of the steps taken to implement the database with evidence._

### Sample Data and Insertion

_Description of the sample data, data sources, and the process of inserting data into the database._

## Use of the Database

### Queries

_Design and implementation of queries with explanations and sample outputs._

### Advanced Features

_Description of advanced features implemented, their use, and evidence of outputs._

### Database Connectivity and Python Implementation

_Description of the database connectivity implementation with evidence._

## Discussion

_Reflection on the work done, achievements, challenges faced, limitations, and potential improvements._

## References

_Report References_
_Code References_

## Pun for good measure
