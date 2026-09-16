---
schema: qual/card@1
id: P-BKF03-4A
kind: problem
title: An irreducible polynomial over $\mathbb Q$ that does not split in its stem field
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
  note: Checked against Problem 4A of the vendored Fall 2003 Berkeley prelim and independently reviewed the accompanying source solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified Eisenstein irreducibility and that the quotient embeds in R, so the two nonreal roots are absent.
---

::: {.problem}
Give an example, with proof, of a nonconstant irreducible polynomial $f ( x )$ over Q with the property that $f ( x )$ does not factor into linear factors over the field $K = \mathbb { Q } [ x ] / ( f ( x ) )$ .
:::
\n\n::: {.solution}\nTake\n\[\nf(x)=x^3-2.\n\]\n\n<1>1. The polynomial $f$ is irreducible over $\mathbb Q$.\n::: {.proof}\nApply Eisenstein's criterion with the prime $2$.
The leading coefficient is not divisible by $2$, every other coefficient is divisible by $2$, and the constant term $-2$ is not divisible by $4$.
Hence $x^3-2$ is irreducible in $\mathbb Q[x]$.\n:::\n\n<1>2. The quotient field\n\[\nK=\mathbb Q[x]/(x^3-2)\n\]\nis isomorphic to $\mathbb Q(\sqrt[3]{2})$, and therefore embeds in $\mathbb R$.\n::: {.proof}\nLet $\alpha=\sqrt[3]{2}\in\mathbb R$.
Since $f$ is irreducible and $f(\alpha)=0$, evaluation at $\alpha$ gives a surjective homomorphism\n\[\n\mathbb Q[x]\longrightarrow\mathbb Q(\alpha)\n\]\nwhose kernel is $(x^3-2)$.
Thus\n\[\nK\cong\mathbb Q(\alpha)\subset\mathbb R.\n\]\n:::\n\n<1>3. The polynomial $f$ does not split into linear factors over $K$.\n::: {.proof}\nOver $\mathbb C$, the three roots are\n\[\n\alpha,\qquad \omega\alpha,\qquad \omega^2\alpha,\n\]\nwhere $\omega=e^{2\pi i/3}$.
The latter two roots are nonreal.
By <1>2, every element of $K$ is real under the displayed embedding, so neither $\omega\alpha$ nor $\omega^2\alpha$ belongs to $K$.
Thus $f$ has only the root $\alpha$ in $K$ and cannot factor completely into linear factors over $K$.\n:::\n\nTherefore $\boxed{f(x)=x^3-2}$ is the required example.\n:::\n
