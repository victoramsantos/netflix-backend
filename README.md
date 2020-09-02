# Netflix Backend

As an home work for my Master of Business Administration class in [Software Engineer](https://www.fiap.com.br/mba/mba-em-engenharia-de-software/) at [FIAP](https://www.fiap.com.br/), we decided to propose a backend implementation for Netflix. 

With this implementation we intend to provide APIs to:
- List movies by gender
- Visualize movie details
- Provide a vote option to like movies
- Provide a reminder list of movies
- Search movies by keyword
- List ranked movies by gender
- Open a technical support for problems
- List watched movies

## Architecture

![Architecture](./assets/architecture.png)

Here we propose a domain driven architecture. We created four Restful microsservices and two backend scripts.

### Movies

The [movies](./movies) microsservice take account of the movie domain. Their APIs answer questions about movie details, genders of movies and searchs for movies.

### Ranking

The [ranking](./ranking) microsservice take account of the votes and movies ranking. Their APIs collect users likes and compute the ranking. Here we also provide a ranking by gender and the top 10 overall movies.

### Reminder

The [reminder](.reminder) microsservice collect the reminder and watch later movies list. Their APIs collect users desire for reminder a movie and to set movies as watched.
