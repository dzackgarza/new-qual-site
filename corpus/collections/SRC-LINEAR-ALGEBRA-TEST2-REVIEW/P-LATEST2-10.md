---
schema: qual/card@1
id: P-LATEST2-10
kind: problem
title: Decode a matrix-encrypted four-letter message
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained PDF extraction for linear_algebra_from_test2.pdf; the source PDF has no usable text layer, so this audit is limited to the preserved extraction generated from that PDF.
---

::: {.problem}
Each letter of a four-letter message is replaced by its position in the alphabet and entered in a $2\times2$ matrix $M$; for example, ``DEAD'' becomes
\[
M=\begin{pmatrix}4&5\\1&4\end{pmatrix}.
\]
The encoded message is $MC$, where
\[
C=\begin{pmatrix}2&-1\\1&1\end{pmatrix}.
\]
If the agent receives
\[
\begin{pmatrix}51&-3\\31&-8\end{pmatrix},
\]
which message was sent?

(A) RUSH  (B) COME  (C) ROME  (D) CALL  (E) not uniquely determined by the information given
:::
