---
schema: qual/card@1
id: E-SS8.EX-16
kind: problem
title: Automorphisms of the disc through the Cayley transform
classification:
  areas:
  - complex-analysis
  topics:
  - Automorphisms
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}
Let
$$
f(z) = \frac{i - z}{i + z} \quad \text{and} \quad f^{-1}(w) = i\frac{1 - w}{1 + w}.
$$

(a) Given $\theta \in \RR$, find real numbers $a, b, c, d$ such that $ad - bc = 1$, and so that for any $z \in \halfplane$
$$
\frac{az + b}{cz + d} = f^{-1}\left( e^{i\theta} f(z) \right).
$$

(b) Given $\alpha \in \DD$ find real numbers $a, b, c, d$ so that $ad - bc = 1$, and so that for any $z \in \halfplane$
$$
\frac{az + b}{cz + d} = f^{-1}\left( \psi_\alpha(f(z)) \right),
$$
with $\psi_\alpha$ defined in Section 2.1.

(c) Prove that if $g$ is an automorphism of the unit disc, then there exist real numbers $a, b, c, d$ such that $ad - bc = 1$ and so that for any $z \in \halfplane$
$$
\frac{az + b}{cz + d} = f^{-1} \circ g \circ f(z).
$$
[Hint: Use parts (a) and (b).]
:::

::: {.solution}
Identify a fractional linear map $z \mapsto \frac{az+b}{cz+d}$ with the matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$, up to a nonzero scalar; composition of maps is the matrix product. Then
$$
f \leftrightarrow \begin{pmatrix} -1 & i \\ 1 & i \end{pmatrix},
\qquad
f^{-1} \leftrightarrow \begin{pmatrix} -i & i \\ 1 & 1 \end{pmatrix},
\qquad
\psi_\alpha(w) = \frac{\alpha - w}{1 - \overline{\alpha} w} \leftrightarrow \begin{pmatrix} -1 & \alpha \\ -\overline{\alpha} & 1 \end{pmatrix}.
$$

::: pf

::: {.pf-step #rotation}
For $\theta \in \RR$, take $a = d = \cos(\theta/2)$, $b = \sin(\theta/2)$, $c = -\sin(\theta/2)$.

::: pf-proof
The rotation $w \mapsto e^{i\theta} w$ corresponds to $\begin{pmatrix} e^{i\theta/2} & 0 \\ 0 & e^{-i\theta/2} \end{pmatrix}$. The product
$$
\begin{pmatrix} -i & i \\ 1 & 1 \end{pmatrix}
\begin{pmatrix} e^{i\theta/2} & 0 \\ 0 & e^{-i\theta/2} \end{pmatrix}
\begin{pmatrix} -1 & i \\ 1 & i \end{pmatrix}
=
\begin{pmatrix} 2\cos(\theta/2) & 2\sin(\theta/2) \\ -2\sin(\theta/2) & 2\cos(\theta/2) \end{pmatrix}
$$
is $2$ times the stated matrix, which has real entries and determinant $\cos^2(\theta/2) + \sin^2(\theta/2) = 1$.
:::

:::

::: {.pf-step #translation}
For $\alpha = p + iq \in \DD$ with $p, q \in \RR$, put $\lambda = \sqrt{1 - \abs{\alpha}^2}$ and take
$$
a = \frac{q}{\lambda},\qquad b = \frac{p-1}{\lambda},\qquad c = \frac{p+1}{\lambda},\qquad d = -\frac{q}{\lambda}.
$$

::: pf-proof
First,
$$
\begin{pmatrix} -1 & \alpha \\ -\overline{\alpha} & 1 \end{pmatrix}
\begin{pmatrix} -1 & i \\ 1 & i \end{pmatrix}
=
\begin{pmatrix} 1 + \alpha & i(\alpha - 1) \\ 1 + \overline{\alpha} & i(1 - \overline{\alpha}) \end{pmatrix}.
$$
Multiplying on the left by the matrix of $f^{-1}$ gives
$$
\begin{pmatrix} i(\overline{\alpha} - \alpha) & \alpha + \overline{\alpha} - 2 \\ 2 + \alpha + \overline{\alpha} & i(\alpha - \overline{\alpha}) \end{pmatrix}
=
\begin{pmatrix} 2q & 2p - 2 \\ 2p + 2 & -2q \end{pmatrix}.
$$
Its entries are real and its determinant is $-4q^2 - (4p^2 - 4) = 4\lambda^2 > 0$. Dividing by $2\lambda$ gives the stated $a, b, c, d$ with $ad - bc = 1$.
:::

:::

::: {.pf-step #general}
For every $g \in \Aut(\DD)$ there are real $a, b, c, d$ with $ad - bc = 1$ and $\frac{az+b}{cz+d} = f^{-1} \circ g \circ f(z)$.

::: pf-proof
By Theorem 2.4 of the chapter, $g(w) = e^{i\theta}\psi_\alpha(w)$ for some $\theta \in \RR$ and $\alpha \in \DD$. Hence
$$
f^{-1} \circ g \circ f = \left(f^{-1} \circ R_\theta \circ f\right) \circ \left(f^{-1} \circ \psi_\alpha \circ f\right),
$$
where $R_\theta(w) = e^{i\theta} w$. By steps [](#rotation){.pf-ref} and [](#translation){.pf-ref}, each factor has a real matrix of determinant $1$. Their product is a real matrix of determinant $1$, and it represents the composition.
:::

:::

::: pf-qed
Steps [](#rotation){.pf-ref}, [](#translation){.pf-ref} and [](#general){.pf-ref} answer (a), (b) and (c).
:::

:::

:::
