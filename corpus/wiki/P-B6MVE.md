---
schema: qual/card@1
id: P-B6MVE
kind: problem
title: 'Let $f: R \to R$ be an endomorphism of $R$ in the category of rings.'
classification:
  areas:
  - algebra
  topics:
  - modules
  - rings
  - homomorphisms
relations: []
review: draft
---

Let $f: R \to R$ be an endomorphism of $R$ in the category of rings.
We can then check that for any $r\in R$, we have $f(r) = f(r 1_R) = rf(1_R)$, which says that $f$ is given by right-multiplication by some fixed element $x_f \definedas f(1_R)$, i.e.
\[
\begin{align*}
f: R &\to R \\
r &\mapsto r \cdot x_f
\end{align*}
\]

and so we can attempt to define
\[
\begin{align*}
\phi_1: \hom_R(R, R) &\to R \\
f &\mapsto x_f \definedas f(1_R)
\end{align*}
\]

We can check that
$$
(g\circ f(r)) = g(f(r)) = g(r\cdot x_f) = r \cdot x_f \cdot x_g,
$$

which shows that in fact
$$
\phi(g \circ f) = x_f \cdot x_g,
$$
which reverses the multiplication.
So the correct codomain is $R^{op}$, and we amend the definition:
\[
\begin{align*}
\phi_2: \hom_R(R, R) &\to R^{op} \\
f &\mapsto x_f \definedas f(1_R)
\end{align*}
\]

By construction, **$\phi_s$ is a ring homomorphism**. If $R$ is commutative, then $x_f \cdot x_g = x_g \cdot x_f$, which makes $\phi_1$ a ring homomorphism as well.
It remains to check that it is an isomorphism/

**$\phi_1$ is in injective**: We can check that $\ker \phi_1 = 0$ as a ring.
To that end, suppose $\phi_1(f) = x_f = 0$.
Then $f(r) = r \cdot 0 = 0$, so $f$ can only be the zero map.

**$\phi_1$ is surjective**: Let $x\in R$ be arbitrary, then we can define $f: R \to R$ by $f(1_R) = x$, so $f(r) = r\cdot x$.
This is an endomorphism of $R$, and thus an element of $\hom_R(R, R)$.

By the first isomorphism theorem for rings, we thus have $\hom_R(R, R) \cong R$.
$\qed$
