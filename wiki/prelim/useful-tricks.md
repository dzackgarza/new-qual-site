---
order: 28
---

# Useful tricks

## Repeated integration by parts

For integrals $\int P(x) e^{ax} \dx$ or $\int P(x) \sin(bx) \dx$ with $P$ a polynomial, each integration by parts with $u$ the polynomial factor lowers its degree by one, so $\deg P + 1$ integrations by parts reduce the integral to an elementary one.

The tabular method records this: one column lists $P$ and its successive derivatives, the other lists $e^{ax}$ (or $\sin(bx)$) and its successive antiderivatives, and the integral is the sum of the products along the diagonals with alternating signs starting from $+$.

::: {.example}
For constants $a,b,c$ and $\omega=n\Omega\neq 0$, the derivatives of $t^3+at^2+bt+c$ are $3t^2+2at+b$, $6t+2a$, $6$, $0$, and successive antiderivatives of $\sin(\omega t)$ are $-\frac{\cos(\omega t)}{\omega}$, $-\frac{\sin(\omega t)}{\omega^2}$, $\frac{\cos(\omega t)}{\omega^3}$, $\frac{\sin(\omega t)}{\omega^4}$.
Pairing them along the diagonals with the signs $+,-,+,-$ gives
\[
\int (t^3+at^2+bt+c)\sin(\omega t)\,dt
=-(t^3+at^2+bt+c)\frac{\cos(\omega t)}{\omega}
+(3t^2+2at+b)\frac{\sin(\omega t)}{\omega^2}
+(6t+2a)\frac{\cos(\omega t)}{\omega^3}
-6\,\frac{\sin(\omega t)}{\omega^4}+C,
\]
and the process stops when the derivatives reach $0$.
:::

::: {.example}
$$
\int x^2 e^x \dx = x^2e^x - 2xe^x + 2e^x + C.
$$
:::

## Power series from the geometric series

| Series | Valid for |
|---|---|
| $\frac{1}{1-x}=\sum_{n\geq 0}x^n=1+x+x^2+x^3+\cdots$ | $x\in(-1,1)$ |
| $e^x=\sum_{n\geq 0}\frac{x^n}{n!}=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots$ | $x\in\RR$ |
| $\cos x=\sum_{n\geq 0}(-1)^n\frac{x^{2n}}{(2n)!}=1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots$ | $x\in\RR$ |
| $\sin x=\sum_{n\geq 0}(-1)^n\frac{x^{2n+1}}{(2n+1)!}=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots$ | $x\in\RR$ |
| $\ln(1+x)=\sum_{n\geq 1}(-1)^{n+1}\frac{x^n}{n}=x-\frac{x^2}{2}+\frac{x^3}{3}-\cdots$ | $x\in(-1,1]$ |
| $\arctan x=\sum_{n\geq 0}(-1)^n\frac{x^{2n+1}}{2n+1}=x-\frac{x^3}{3}+\frac{x^5}{5}-\cdots$ | $x\in[-1,1]$ |

Since $\cos$ is even and $\sin$ is odd, their series contain only even and only odd powers respectively; substituting into the exponential series gives, for example, $e^{17x}=\sum_{n\geq 0}\frac{17^nx^n}{n!}$.

For $\abs x<1$, $\sum_{n\geq0} x^n = \frac{1}{1-x}$.
Differentiating term by term gives $\sum_{n\geq1} n x^{n-1} = \frac{1}{(1-x)^2}$, and multiplying by $x$ gives $\sum_{n\geq1} n x^n = \frac{x}{(1-x)^2}$.
Repeating the operation $x\frac{d}{dx}$ gives $\sum_n n^kx^n$ for each $k\geq 1$.
