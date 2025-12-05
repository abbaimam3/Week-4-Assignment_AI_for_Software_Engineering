# Part 3: Ethical Reflection

## 1. Potential Biases in the Predictive Model

When deploying an AI model to predict software issue priority, several biases might inadvertently creep in, affecting fairness and team dynamics:

### A. Reporter Role Bias (Authority Bias)
*   **The Issue:** The model might learn to assign higher priority to issues reported by "Developers" or "Managers" while systematically downgrading issues reported by "Users" or "QA," even if the user-reported issue is critical (e.g., a crash in production).
*   **Impact:** This creates a two-tiered system where end-user feedback is ignored, leading to customer dissatisfaction and a product that serves internal metrics rather than user needs.

### B. Team Size/Resource Bias
*   **The Issue:** If the training data shows that larger teams (with more resources) close tickets faster or have them marked as "High Priority" more often, the model might learn to deprioritize issues from smaller, under-resourced teams.
*   **Impact:** Under-represented teams or experimental projects might struggle to get their critical issues addressed, reinforcing a cycle of neglect.

### C. Historical Bias
*   **The Issue:** If the historical data reflects past human prejudices (e.g., a specific legacy component was always ignored), the AI will codify and automate this neglect.
*   **Impact:** Technical debt in specific areas becomes "institutionally approved" by the AI, making it harder to advocate for necessary refactoring.

## 2. Addressing Biases with IBM AI Fairness 360

IBM AI Fairness 360 (AIF360) is an open-source toolkit that can help detect and mitigate these biases throughout the AI lifecycle.

### A. Detection (Metrics)
*   **Disparate Impact:** We can calculate the *Disparate Impact* metric to see if the ratio of "High Priority" predictions for "Users" is significantly lower than for "Developers."
*   **Equal Opportunity Difference:** We can check if the True Positive Rate (correctly identifying a high-priority issue) is the same across all reporter roles.

### B. Mitigation (Algorithms)
*   **Pre-processing (Reweighing):** Before training, we can use *Reweighing* to assign higher weights to training examples from under-represented groups (e.g., critical issues reported by Users) to make the training data more balanced.
*   **In-processing (Adversarial Debiasing):** We can use *Adversarial Debiasing* to train the model to maximize accuracy while simultaneously minimizing the ability of an adversary to guess the protected attribute (e.g., Reporter Role) from the prediction.
*   **Post-processing (Calibrated Equalized Odds):** After the model makes predictions, we can adjust the decision threshold for different groups to ensure that the error rates are comparable, ensuring that a "High Priority" label means the same urgency regardless of who reported it.

**Conclusion:**
Deploying AI in software engineering is not just a technical challenge but a socio-technical one. Tools like AIF360 are essential to ensure our automation tools do not amplify existing organizational flaws.
