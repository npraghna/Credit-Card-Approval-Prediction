# 3. Project Design Phase

## System Architecture
The Credit Card Approval Prediction System follows a standard Model-View-Controller (MVC) inspired design:

- Frontend (View): HTML templates provide the user interface where applicants input their details.
- Backend (Controller): Flask handles HTTP requests, processes form data, and interacts with the model.
- Model Layer: The pre-trained machine learning model (e.g., Logistic Regression or Random Forest) makes predictions based on the processed data.

## Workflow Diagram
1. User Input: User fills out the web form on the homepage.
2. Data Preprocessing: Input data is cleaned and transformed to match the model's training format.
3. Prediction: The backend passes the data to the `.pkl` model file.
4. Response: The system returns the predicted outcome (Approved/Rejected) to the `result.html` page.

## Database Design (Conceptual)
While this version uses a file-based model, future iterations will include:
- User Database: To store application history and applicant profiles.
- Audit Logs: To track prediction requests and model performance over time.

## Design Considerations
- Scalability: Modular code structure to allow future model updates.
- Security: Input validation to prevent malicious data injection.
- User Experience (UX): Simple, clean interface for ease of use.
-