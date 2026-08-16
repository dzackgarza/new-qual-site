---
schema: qual/card@1
id: P-OETKP
kind: problem
title: Let $R = C[0, 1]$ be the ring of continuous real-valued functions on the...
classification:
  areas:
  - algebra
  topics:
  - maximal-ideals
  - ideals
  - rings
relations: []
review: draft
---

::: problem
Let $R = C[0, 1]$ be the ring of continuous real-valued functions on the interval $[0, 1]$.
Let I be an ideal of $R$.

(a) Show that if $f \in I, a \in [0, 1]$ are such that $f (a) \neq 0$, then there exists $g \in I$ such that $g(x) \geq 0$ for all $x \in [0, 1]$, and $g(x) > 0$ for all $x$ in some open neighborhood of $a$.

(b) If $I \neq R$, show that the set $Z(I) = \{x \in [0, 1] \suchthat f(x) = 0 \text{ for all } f \in I\}$ is nonempty.

(c) Show that if $I$ is maximal, then there exists $x_0 \in [0, 1]$ such that $I = \{ f \in R \suchthat f (x_0 ) = 0\}$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**(a) Constructing $g \in I$:**
Define $g = f^2 = f \cdot f$.
Since $I$ is an ideal and $f \in I$, $g = f \cdot f \in I$.
For any $x \in [0, 1]$, $g(x) = (f(x))^2 \geq 0$.
Since $f$ is continuous and $f(a) \neq 0$, $g(a) = (f(a))^2 > 0$.
By continuity of $g$, there exists an open neighborhood $U$ of $a$ in $[0, 1]$ such that $g(x) > 0$ for all $x \in U$.

**(b) $Z(I)$ is non-empty for any proper ideal $I \subsetneq R$:**
Suppose towards a contradiction that $Z(I) = \emptyset$.
This means that for every point $a \in [0, 1]$, there exists some $f_a \in I$ such that $f_a(a) \neq 0$.
By part (a), for each $a \in [0, 1]$, there exists $g_a \in I$ and an open neighborhood $U_a$ of $a$ such that $g_a(x) \geq 0$ everywhere and $g_a(x) > 0$ for all $x \in U_a$.
The collection $\{U_a\}_{a \in [0, 1]}$ forms an open cover of the compact space $[0, 1]$.
By compactness, there is a finite subcover $U_{a_1}, U_{a_2}, \ldots, U_{a_k}$.
Define:
$$
h(x) = \sum_{j=1}^k g_{a_j}(x).
$$
Since each $g_{a_j} \in I$, the sum $h \in I$.
For any $x \in [0, 1]$, $x \in U_{a_j}$ for some $j \in \{1, \ldots, k\}$, so $g_{a_j}(x) > 0$. Since all $g_{a_i} \geq 0$, we have $h(x) > 0$ for all $x \in [0, 1]$.
Since $h$ is continuous and strictly positive on the compact set $[0, 1]$, $h$ is a unit in $R = C[0, 1]$ (its reciprocal $1/h$ is continuous).
Since $I$ contains the unit $h$, $I = R$, contradicting that $I \subsetneq R$ is a proper ideal.
Hence $Z(I) \neq \emptyset$.

**(c) Maximal ideals of $C[0, 1]$ are point-evaluations:**
Let $I \subsetneq R$ be a maximal ideal.
By part (b), $Z(I)$ is non-empty, so pick $x_0 \in Z(I)$.
Then for all $f \in I$, $f(x_0) = 0$.
Let $M_{x_0} = \{f \in R \mid f(x_0) = 0\}$.
Then $M_{x_0}$ is the kernel of the evaluation homomorphism $\operatorname{ev}_{x_0}: C[0, 1] \to \RR$, which is surjective onto the field $\RR$.
Thus $M_{x_0}$ is a maximal ideal of $R$.
Since $f(x_0) = 0$ for all $f \in I$, we have $I \subseteq M_{x_0} \subsetneq R$.
Since $I$ is a maximal ideal and $M_{x_0} \neq R$, we must have:
$$
I = M_{x_0} = \{f \in C[0, 1] \mid f(x_0) = 0\}.
$$
:::
