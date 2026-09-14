---
schema: qual/card@1
id: P-HM21B18-FIN-06
kind: problem
title: Barycentric-refinement eigenvectors and a closed discrete dynamical system
classification: {areas: [applied-algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $\vec x=(v,e,f)^T$ record the numbers of vertices, edges, and faces of a polyhedron. Under barycentric refinement suppose
\[
A=\begin{pmatrix}1&1&1\\0&2&6\\0&0&6\end{pmatrix}
\]
acts on $\vec x$.

(a) Verify that
\[
v_1=\begin{pmatrix}1\\0\\0\end{pmatrix},\quad
v_2=\begin{pmatrix}1\\1\\0\end{pmatrix},\quad
v_3=\begin{pmatrix}1\\3\\2\end{pmatrix}
\]
are eigenvectors and find their eigenvalues.

(b) Find a closed form for $\vec x(t+1)=A\vec x(t)$ with initial condition
\[
\vec x(0)=\begin{pmatrix}7\\12\\6\end{pmatrix}.
\]
:::
