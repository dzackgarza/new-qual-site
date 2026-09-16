---
schema: qual/card@1
id: P-GREPT-57
kind: problem
title: "Flaw in a proof of Cauchy's mean value formula"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 57 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Cauchy's Mean-Value formula says that if $f$ and $g$ are two functions that are continuous on the nonempty, closed interval $[a, b]$ and differentiable on $(a, b)$, then there exists at least one number $c$, with $a < c < b$, such that:

$$g'(c)[f(b) - f(a)] = f'(c)[g(b) - g(a)]$$

Consider the following argument:

(1) "The functions $f$ and $g$ in the result above satisfy the hypotheses of the Mean-Value theorem, so there exists a number $c$, with $a < c < b$, such that

$$f'(c) = \frac{f(b) - f(a)}{b - a} \quad \text{and} \quad g'(c) = \frac{g(b) - g(a)}{b - a}.\text{"}$$

(2) "The equations in Step (1) imply that

$$b - a = \frac{f(b) - f(a)}{f'(c)} \quad \text{and} \quad b - a = \frac{g(b) - g(a)}{g'(c)}.\text{"}$$

(3) "The equations in Step (2) imply that

$$\frac{f(b) - f(a)}{f'(c)} = \frac{g(b) - g(a)}{g'(c)}.\text{"}$$

(4) "Cross multiplying, we get $g'(c)[f(b) - f(a)] = f'(c)[g(b) - g(a)]$."

Which of the following statements is/are true?

I. Step (1) is not valid.

II. The conclusion of Step (1) does not imply the result of Step (2).

III. The conclusion of Step (2) does not imply the result of Step (3).

IV. The conclusion of Step (3) does not imply the result of Step (4).

(A) I only
(B) II only
(C) I and II only
(D) IV only
(E) None are true; the argument is a valid proof of Cauchy's Mean-Value formula.
:::
