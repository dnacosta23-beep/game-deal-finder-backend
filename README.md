# Game Deal Finder Backend

A Flask REST API that searches the CheapShark API for game deals and stores user-saved games in Supabase.

The backend acts as the middle layer between the React frontend, the CheapShark API, and the Supabase database.

---

## Live API

https://YOUR-RENDER-BACKEND.onrender.com

---

## Frontend

https://YOUR-CLOUDFRONT-URL

---

## Features

- Search game deals
- Retrieve saved games
- Save new game deals
- Delete saved games
- Connect to CheapShark API
- Store favorites in Supabase
- REST API endpoints

---

## Built With

- Python
- Flask
- Flask-CORS
- Supabase
- Requests
- Gunicorn
- Render

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/game-deal-finder-backend.git
```

Navigate into the project

```bash
cd game-deal-finder-backend
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

Mac/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
SUPABASE_URL=your_supabase_url

SUPABASE_KEY=your_supabase_key

FRONTEND_URL=https://YOUR-CLOUDFRONT-URL
```

Run locally

```bash
flask run
```

or

```bash
python app.py
```

---

## API Endpoints

### Search Deals

```
GET /api/deals?title=palworld
```

Returns matching game deals from CheapShark.

---

### Get Saved Games

```
GET /saved
```

Returns all saved games stored in Supabase.

---

### Save Game

```
POST /saved
```

Stores a selected game in Supabase.

Example JSON

```json
{
  "title": "Palworld",
  "store": "Steam",
  "sale_price": 19.99,
  "normal_price": 29.99,
  "thumb": "...",
  "deal_url": "..."
}
```

---

### Delete Saved Game

```
DELETE /saved/<id>
```

Deletes a saved game from Supabase.

---

## Database

Supabase stores:

- Game title
- Store
- Sale price
- Normal price
- Savings
- Thumbnail
- Deal URL

---

## Deployment

Backend deployed using:

- Render

Frontend deployed using:

- AWS S3
- AWS CloudFront

---

## Future Improvements

- User accounts
- Duplicate save prevention
- Search history
- Pagination
- Price alerts
- Steam authentication