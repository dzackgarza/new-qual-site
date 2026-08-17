---
schema: qual/card@1
id: P-DYEG6
kind: problem
title: "Let $L/K$ be a finite extension of fields."
classification:
  areas:
  - algebra
  topics:
  - separability
  - field-extensions
  - finite-fields
relations: []
review: draft
solved: true
---
Let $L/K$ be a finite extension of fields.

a.
Define what it means for $L/K$ to be *separable*.

b.
Show that if $K$ is a finite field, then $L/K$ is always separable.

c.
Give an example of a finite extension $L/K$ that is not separable.


:::{.solution}
\envlist

- $L/k$ is **separable** iff every element $\alpha$ is separable, i.e. the minimal polynomial $m(x)$ of $\alpha$ is a separable polynomial, i.e. $m(x)$ has no repeated roots in (say) the algebraic closure of $L$ (or just any splitting field of $m$).

- If $\ch k = p$, suppose toward a contradiction that $L/k$ is not separable.
  Then there is some $\alpha$ with an inseparable (and irreducible) minimal polynomial $f(x)\in k[x]$.
- Claim: since $f$ is inseparable and irreducible, $f(x) = g(x^p)$ for some $g\in k[x]$.
  - Note: write $g(x) \da \sum a_k x^k$, so that $f(x) = \sum a_k (x^p)^k = \sum a_k x^{pk}$.
- This is a contradiction, since it makes $f$ reducible by using the "Freshman's dream":
\[
f(x) = \sum a_k x^{pk} = \qty{ \sum a_k^{1\over p} x^k}^p \da (h(x))^p 
.\]

- Proof of claim: in $\ch k = p, f$ inseparable $\implies f(x) = g(x^p)$. 
  - Use that $f$ is inseparable iff $\gcd(f, f') \neq 1$, and since $f$ is irreducible this forces $f' \equiv 0$, so $ka_k = 0$ for all $k$.
  - Then $a_k\neq 0$ forces $p\divides k$, so $f(x) = a_0 + a_px^p + a_{2p}x^{2p} + \cdots$ and one takes $g(x) \da \sum a_{kp}x^{kp}$.

- A finite inseparable extension:
  - It's a theorem that finite extensions of perfect fields are separable, so one needs a non-perfect field.
  - Take $L/k \da \FF_p(t^{1\over p}) / \FF_p(t)$, which is a degree $p$ extension (although both fields are infinite are characteristic $p$).
  - Then the minimal polynomial of $t$ is $f(x) \da x^p - t \in \FF_p(t)[x]$, where $f'(x) = px^p \equiv 0$
    Alternatively, just note that $f$ factors as $f(x) = (x-t^{1\over p})^p$ in $L[x]$, which has multiple roots.
:::


