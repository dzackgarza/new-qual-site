---
schema: qual/card@1
id: S-PIFFO
kind: solution
title: Solution to P-TB7BG
classification:
  areas:
  - prelim
  topics: []
relations:
- kind: solves
  target: P-TB7BG
review: draft
---

::: {.solution}
A square matrix $N$ is nilpotent iff $N^\alpha=0$ for some $\alpha$.
We wish to show that every nilpotent matrix is similar to a matrix of the form $$\begin{bmatrix}N_1&&&\\&N_2&&\\&&\ddots&\\&&&N_s\end{bmatrix}$$ where each $N_i$ is a square matrix of the form $$\begin{bmatrix}0&&&&\\1&0&&&\\&1&\ddots&&\\&&\ddots&0&\\&&&1&0\end{bmatrix}$$ We say two matrices are similar just in case they have the same rational canonical form.
So suppose $A$ is a nilpotent matrix.
Therefore, $$A^\alpha=0\Rightarrow\underbrace{A\cdot A\cdots A}_{\alpha}=0\Rightarrow\underbrace{(A-0I)(A-0I)\cdots(A-0I)}_{\alpha}=0$$ $$\Rightarrow A\text{ is a root for the polynomial }\underbrace{(x-0)(x-0)\cdots(x-0)}_{\alpha}\Rightarrow A\text{ is a root for }\underbrace{x\cdot x\cdots x}_{\alpha}\Rightarrow x^\alpha\text{ is the minimal polynomial for }A$$ This minimal polynomial will yield the following $\alpha\times\alpha$ companion matrix: $$\begin{bmatrix}0&&&\\1&0&&\\&1&\ddots&\\&&\ddots&0\\&&&1&0\end{bmatrix}$$ Furthermore, any other invariant factor of $A$ must divide $x^\alpha$, so it must be of the form $x^{\beta_i}$, with $\beta_1\mid\beta_2\mid\dots\mid\beta_n\mid\alpha$.
Each of these invariant factors will give a $\beta_i\times\beta_i$ matrix of the same companion form.
Now, using these companion matrices to construct the rational canonical form for $A$ we will get a matrix of the form: $$\begin{bmatrix}M_1&&&\\&M_2&&\\&&\ddots&\\&&&M_t\end{bmatrix}$$ Where the $M_i$'s are the square companion matrices as described above.
Clearly this is similar to the desired matrix.
:::
