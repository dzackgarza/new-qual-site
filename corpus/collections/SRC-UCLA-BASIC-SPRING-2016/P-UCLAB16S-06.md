---
schema: qual/card@1
id: P-UCLAB16S-06
kind: problem
title: Open and closed balls in an ultrametric
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Spring 2016, `assets/attachments/basic-16S.pdf`.
---

::: {.problem}
A metric $\rho$ on a metric space $(X,\rho)$ is an ultrametric if
\[
\rho(x,y)\le \max\{\rho(x,z),\rho(y,z)\}
\qquad\text{for all }x,y,z\in X.
\]
Prove that every open ball $\{y:\rho(x,y)<r\}$ is closed and every closed ball $\{y:\rho(x,y)\le r\}$ is open.
:::
