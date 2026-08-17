---
schema: qual/card@1
id: P-W3PZY
kind: problem
title: "Let $f(x) \\in F[x]$ be irreducible, then since $p(x) \\definedas \\gcd(f, f')$ must divide $f$ and $f$ is\u2026"
classification:
  areas:
  - algebra
  topics:
  - separability
  - characteristic
  - irreducibility-criteria
relations: []
review: draft
solved: false
---

::: problem
Let $f(x) \in F[x]$ be irreducible, then since $p(x) \definedas \gcd(f, f')$ must divide $f$ and $f$ is irreducible, the only possibilities are $p(x) = 1$ or $p(x) = f(x)$.

If $p(x) = 1$, then $f$ is separable, so every root is distinct and $f$ itself is of the form $f(x^{p^e})$ where each $e=0$.

Otherwise, $p(x) = f(x)$, which forces $f'(x) = 0$ in $K[x]$.
If we write
\[
\begin{align*}
f(x) &= \sum_{k=0}^n a_k a^k \\
f'(x) &= \sum_{k=1}^n k a_k a^{k-1} \\
,\end{align*}
\]
then $f'(x) \equiv 0$ forces either $a_k = 0$, or $k = 0$ in $F$ (so $p \divides k$).

We can thus rewrite $f$ by leaving out all terms where $a_k = 0$ to obtain
$$
f(x) = a_p x^p + a_{2p} x^{2p} + \cdots
$$
and we thus define
$$
g(x) \definedas a_p x + a_{2p}x^{2} + \cdots 
$$

and we recover $f(x) = g(x^p)$.
Moreover, $g$ is irreducible; otherwise if $h(x) \divides g(x)$ then $h(x^p) \divides g(x^p) = f$, where $f$ was assumed irreducible.
If $g$ is separable we are done; otherwise $g$ fulfills the same hypotheses of that applied to $f$, so we can inductively continue this process to write $g(x) = g_1(x^p)$, and thus $f(x) = g(x^p) = g_1(x^{p^2})$, and so on.

To see that every root of $f$ has multiplicity $p^e$, note that if $f(\alpha) = 0$ then $g(\alpha^{p^e}) = 0$.
But $g$ is separable, so $(x - \alpha^{p^e}) \divides g(x)$ in $K[x]$ and thus $(x^{p^e} - \alpha^{p^e}) \divides g(x^{p^e}) = f$ in $\overline{K}[x]$ where $\overline K$ is an algebraic closure of $K$.
But then $x^{p^e} - \alpha^{p^e} = (x-\alpha)^{p^e} \divides f(x)$, which precisely says that $\alpha$ is a root of multiplicity $p^e$.
:::
