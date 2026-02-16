# 🚀 TaskLab — Django Background Jobs Done the Engineering Way

> “Because `sleep(5)` inside a request is a crime.”

TaskLab is a deliberately engineered Django project built to demonstrate how to move from **blocking request-based execution** to a **proper distributed background job architecture** using Celery and Redis.

This is not a tutorial toy app.
It is a systems-thinking sandbox.

It exists to answer one question:

> What actually happens when we move work outside the HTTP request lifecycle?

---

# 🎯 Purpose of This Project

Most Django apps start like this:

```python
def post(self, request):
    sleep(5)
    return JsonResponse({"done": True})
```

It works.

Until it doesn’t.

Under load:

- Workers block
- Requests queue up
- Throughput collapses
- Everyone blames Django

This project demonstrates:

- Why blocking inside requests is dangerous
- How to decouple execution using a broker
- How background workers actually behave
- How task state flows through a distributed system
- How to observe and poll async jobs correctly

---

# 🧠 What This Project Demonstrates

## 1️⃣ Process Separation

We run three independent runtimes:

```
Django (Producer)
Redis (Broker)
Celery Worker (Consumer)
```

Each has:

- Separate memory
- Separate lifecycle
- Separate failure modes

This is real distributed architecture — not async syntax sugar.

---

## 2️⃣ Proper Background Job Flow

1. HTTP request enqueues task
2. Redis stores message
3. Worker picks task
4. Worker executes ORM logic
5. Result stored in database
6. Frontend polls for completion

No blocking.
No magic.
No lies.

---

## 3️⃣ Result Persistence via Database

Instead of using Redis as result backend, this project uses:

```
django-celery-results
```

Why?

Because:

- Results are inspectable
- Admin observability is easy
- State transitions are visible
- Debugging is transparent

Recruiters like observability.

---

# 🏗 Architecture Overview

## Backend Stack

- Django
- Celery
- Redis
- SQLite (for demo purposes)
- django-celery-results

## Frontend Stack

- Django Templates
- Alpine.js
- TailwindCSS

No SPA framework.
No unnecessary complexity.
Just enough UI to observe async behavior.

---

# 📂 Project Structure

```
config/
    settings.py
    celery.py
    urls.py

tasklab/
    views.py
    tasks.py
    templates/
```

### Key Files

- `config/celery.py`
  Defines Celery application and integrates with Django settings.

- `tasklab/tasks.py`
  Contains distributed task definitions.

- `tasklab/views.py`
  Enqueues tasks and exposes result endpoints.

- `home.html`
  Polls task status using Alpine.js.

---

# 🔄 Task Lifecycle

When a task is triggered:

```
POST /  → slow_task.delay()
```

Celery:

- Generates task ID
- Pushes message to Redis
- Returns immediately

Worker:

- Picks task
- Executes
- Writes result to DB

Frontend:

- Polls `/slow-task/<task_id>`
- Displays result when ready

---

# 🧪 What This Proves

- Non-blocking request handling
- Separation of request lifecycle and execution lifecycle
- State persistence
- Distributed communication via broker
- Background processing under Windows (`--pool=solo`)

---

# 📊 Why This Matters

This project demonstrates understanding of:

- Distributed systems fundamentals
- Process boundaries
- Broker-based communication
- Failure surfaces
- Task state transitions
- Observability patterns

This is not just “I used Celery.”

This is:

> “I understand why Celery exists.”

---

# 🖥 Running the Project

### Start Redis

```
redis-server
```

### Start Django

```
python manage.py runserver
```

### Start Celery Worker (Windows)

```
celery -A config worker --loglevel=info --pool=solo
```

Then visit:

```
http://127.0.0.1:8000/
```

Trigger a task and watch:

- Worker logs
- Admin panel
- UI polling

---

# 📈 Future Extensions (If You’re Curious)

- Retry policies
- Exponential backoff
- Task chaining
- Dead letter queues
- Idempotency handling
- Concurrency pools (Linux prefork)
- Production-ready Redis config
- Monitoring integrations

This sandbox is designed to evolve.

---

# 👨‍💻 About the Author

Backend engineer focused on:

- Architecture > hacks
- Systems thinking > shortcuts
- Understanding execution models deeply

If you’re hiring someone who:

- Knows what happens after `.delay()`
- Understands process isolation
- Thinks in lifecycles, not just endpoints

We should talk.

---

# 🧩 Final Note

This project is intentionally small.

Because clarity scales better than complexity.

And yes — I removed `sleep(5)` from the request.
You're welcome.
