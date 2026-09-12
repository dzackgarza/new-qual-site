---
schema: qual/card@1
id: P-ALGS26F
kind: problem
title: "Finite field extension via x^4+x+1 over F_2"
classification:
  areas:
  - algebra
  topics:
  - Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $f(x) = x^4 + x + 1 \in \mathbb{F}_2[x]$.
Let $E = \mathbb{F}_2[x]/\langle f \rangle$.

(a) Show that $E$ is a field.

(b) Let $\alpha = (x^2 + x) + \langle f \rangle \in E$.
Find the number of elements in $\mathbb{F}_2(\alpha)$.
:::

::: {.solution}
<1>1. The polynomial \(f(x)=x^4+x+1\) has no root in \(\mathbb F_2\).
::: {.proof}
One has \(f(0)=1\) and \(f(1)=1+1+1=1\) in \(\mathbb F_2\). Thus \(f\) has no linear factor.
:::

<1>2. The polynomial \(f\) has no irreducible quadratic factor.
::: {.proof}
The only monic irreducible quadratic over \(\mathbb F_2\) is \(q(x)=x^2+x+1\): the other monic quadratics have a root in \(\mathbb F_2\). If a degree-four polynomial over a field is reducible and has no linear factor, it is a product of two irreducible quadratics.
Hence, if \(f\) were reducible, both quadratic factors would have to equal \(q\), so
\[
f(x)=q(x)^2=(x^2+x+1)^2=x^4+x^2+1,
\]
which is false.
:::

<1>3. Therefore \(f\) is irreducible, so
\[
E=\mathbb F_2[x]/(f)
\]
is a field with \(2^4=16\) elements.
::: {.proof}
A quotient \(k[x]/(f)\) is a field exactly when \(f\) is irreducible.
Since \(\deg f=4\), the quotient is a four-dimensional vector space over \(\mathbb F_2\), hence has \(2^4\) elements.
This proves part (a).
:::

<1>4. Let \(\beta=x+(f)\in E\). Then \(\beta^4=\beta+1\), and for \(\alpha=\beta^2+\beta\) one has
\[
\alpha^2=\alpha+1.
\]
::: {.proof}
The relation \(f(\beta)=0\) gives \(\beta^4+\beta+1=0\), hence \(\beta^4=\beta+1\). In characteristic \(2\),
\[
\alpha^2=(\beta^2+\beta)^2=\beta^4+\beta^2=(\beta+1)+\beta^2=\alpha+1.
\]
Thus \(\alpha^2+\alpha+1=0\).
:::

<1>5. The element \(\alpha\) does not lie in \(\mathbb F_2\), so its minimal polynomial over \(\mathbb F_2\) is \(t^2+t+1\).
::: {.proof}
The polynomial \(t^2+t+1\) has no root in \(\mathbb F_2\), hence is irreducible.
By <1>4, \(\alpha\) is a root, so its minimal polynomial is this quadratic.
:::

<1>6. Therefore
\[
[\mathbb F_2(\alpha):\mathbb F_2]=2,
\qquad
|\mathbb F_2(\alpha)|=2^2=4.
\]
::: {.proof}
The extension degree equals the degree of the minimal polynomial from <1>5. A degree-two extension of \(\mathbb F_2\) has four elements.
This proves part (b).
:::
:::
