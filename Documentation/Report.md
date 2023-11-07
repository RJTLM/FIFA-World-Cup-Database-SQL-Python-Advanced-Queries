# Entity Sets, Relationship Sets, and Cardinality Constraints

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
