---
schema: qual/card@1
id: P-VYRJF
kind: problem
title: $\lim_{n\to\infty}\int_0^n(1+x^2/n)^{-(n+1)}\,dx$
classification:
  areas:
  - real-analysis
  topics:
  - convergence-of-integrals
  - integrals
relations: []
review: draft
solved: true
---
Compute the following limit and justify your calculations:
\[
\lim_{n\to\infty} \int_0^n \qty{1 + {x^2 \over n}}^{-(n+1)} \,dx
.\]

:::{.solution}
:::{.concept}
- DCT
- Passing limits through products and quotients
:::

Note that 
\[
\lim_{n} \qty{1 + {x^2 \over n}}^{-(n+1)} 
&= {1 \over \lim_{n} \qty{1 + {x^2 \over n}}^1 \qty{1 + {x^2 \over n}}^n } \\
&= {1 \over 1 \cdot e^{x^2}} \\
&= e^{-x^2}
.\]

If passing the limit through the integral is justified, we will have
\[
\lim_{n\to\infty} \int_0^n \qty{ 1 + {x^2\over n}}^{-(n+1)}\, dx 
&= \lim_{n\to\infty} \int_\RR \chi_{[0, n]} \qty{ 1 + {x^2\over n}}^{-(n+1)} \, dx  \\
&= \int_\RR \lim_{n\to\infty} \chi_{[0, n]} \qty{ 1 + {x^2\over n}}^{-(n+1)} \, dx  \qtext{by the DCT} \\
&= \int_\RR \lim_{n\to\infty} \qty{ 1 + {x^2\over n}}^{-(n+1)} \, dx  \\
&= \int_0^\infty e^{-x^2}  \\
&= {\sqrt \pi \over 2}
.\]

Computing the last integral:

\[
\qty{\int_\RR e^{-x^2}\, dx}^2
&= \qty{\int_\RR e^{-x^2}\,dx} \qty{\int_\RR e^{-y^2}\,dx} \\
&= \int_\RR \int_\RR e^{-(x+y)^2}\, dx \\
&= \int_0^{2\pi} \int_0^\infty e^{-r^2} r\, dr \, d\theta \qquad u=r^2 \\
&= {1\over 2} \int_0^{2\pi } \int_0^\infty e^{-u}\, du \, d\theta \\
&= {1\over 2} \int_0^{2\pi} 1 \\
&= \pi
,\]
and now use the fact that the function is even so $\int_0^\infty f = {1\over 2} \int_\RR f$.

Justifying the DCT:

- Apply Bernoulli's inequality: 
\[
{1 + {x^2\over n}}^{n+1} \geq {1 + {x^2\over n}}\qty{1 + x^2} \geq {1 + x^2}
,\]
  where the last inequality follows from the fact that $1 + {x^2 \over n} \geq 1$
:::

