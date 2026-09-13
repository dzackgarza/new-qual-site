# Eval: nvidia/nemotron-3-super-120b-a12b:free

- Run timestamp (UTC): 20260912T085503Z
- Model timestamp (UTC): 20260912T092533Z
- Model: `nvidia/nemotron-3-super-120b-a12b:free`
- Provider: `nvidia`
- Success: True
- Usage: {"prompt_tokens": 3646, "completion_tokens": 9401, "total_tokens": 13047, "cost": 0, "is_byok": false, "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0, "audio_tokens": 0, "video_tokens": 0}, "cost_details": {"upstream_inference_cost": 0, "upstream_inference_prompt_cost": 0, "upstream_inference_completions_cost": 0}, "completion_tokens_details": {"reasoning_tokens": 4155, "image_tokens": 0, "audio_tokens": 0}}
- Problem source: `HARD-PROOF-EVAL.md` verbatim (Koebe-Bieberbach)
- Prompt length: 8778 chars
- Max tokens: per-model saturated (235929), timeout: none

---

## Chain-of-Thought (reasoning)

We need to produce a full solution with proofs for each part (a)-(g). The problem statement is given. The solution skeleton is provided in the prompt but we need to flesh out details, ensure rigorous proofs, correct any mistakes, and present a clean solution.

We need to show:

(a) No uniform r exists without further restrictions: Provide sequence f_n(z)=z/n, show f_n'(0)=1/n →0, and 1/n not in image.

(b) Even with f'(0)=1, no uniform r: Use f_ε(z)=ε(e^{z/ε} -1). Show f_ε(0)=0, f_ε'(0)=1, image omits -ε, so for any r>0 choose ε<r then -ε∈D_r(0) not in image.

(c) For h(z)=1/z + c_0 + c_1 z + ... injective on punctured disc, prove sum n|c_n|^2 ≤1. Use area theorem (Gronwall's area theorem). Compute area of complement of h(D_ρ\{0}) as π(1/ρ^2 - Σ n|c_n|^2 ρ^{2n})≥0. Then let ρ→1.

(d) Given f(z)=z+ a_2 z^2+... injective with f(0)=0, f'(0)=1, construct g such that g^2(z)=f(z^2). Show f(z)/z nowhere vanishing, define ψ holomorphic sqrt with ψ(0)=1, set g(z)=z ψ(z^2). Show g injective, g(0)=0, g'(0)=1.

(e) Using (c) on 1/g, bound |a_2|≤2, equality case yields Koebe function. Need to compute expansion: g(z)=z + b_2 z^3+..., then 1/g(z)=1/z - b_2 z +..., apply (c) to get |b_2|≤1, thus |a_2|=2|b_2|≤2. Equality forces 1/g(z)=1/z + e^{iθ} z, thus g(z)=z/(1+ e^{iθ}z^2). Then f(z)=z/(1+ e^{iθ}z)^2.

(f) If h injective on disc and avoids two values z1,z2, then |z1 - z2| ≤4. Consider functions 1/(h(z)-z_j) which are injective with simple pole at 0. Expand: 1/(h(z)-z_j)=1/z + α_{0j}+ α_{1j} z+... Apply (c) to get |α_{1j}|≤1. Then relate α_{1j} to z_j: compute expansion: Since h(z)=z+ a_2 z^2+..., then h(z)-z_j = -z_j + z + a_2 z^2+...; its reciprocal expansion yields coefficient of z equals something like (1+z_j^2?) Actually need to derive correctly. Standard proof: For univalent f(z)=z+ a_2 z^2+..., the function 1/f(z) = 1/z - a_2 + ...? Wait compute: f(z)=z+ a_2 z^2+ a_3 z^3+... Then 1/f(z) = (1/z) * 1/(1+ a_2 z+ a_3 z^2+...) = (1/z)(1 - a_2 z + (a_2^2 - a_3) z^2+...). So 1/f(z) = 1/z - a_2 + (a_2^2 - a_3) z + ... So coefficient of z is a_2^2 - a_3. Not directly a_2. However for the function 1/(f(z)-w) we can get linear term related to w. There's known inequality: |z1 - z2| ≤ 4 for omitted values of a univalent function normalized f(0)=0, f'(0)=1. This is a corollary of Bieberbach's coefficient bound |a_2| ≤2. Actually the proof: If f omits w1 and w2, then consider g(z)= (f(z)-w1)/(f(z)-w2) which maps disc into disc omitting 0 and ∞? Hmm.

But the problem's hint: Look at second coefficient in power series expansion of 1/(h(z)-z_j). So they want to compute expansion of 1/(h(z)-z_j) = 1/z + c_0 + c_1 z + ... and relate c_1 to z_j. Let's derive.

Let h(z) be injective on D, with h(0)=0, h'(0)=1? Actually part (f) says: If h(z) = 1/z + c_0 + c_1 z + ... is injective on D and avoids the values z1 and z2, show |z1 - z2| ≤4. Wait they defined h(z) as having a pole at 0 (like 1/z + ...). That's the form of 1/f(z) after normalization? Actually if f is univalent normalized, then 1/f(z) has a simple pole at 0 with residue 1, expansion 1/z - a_2 + ... So indeed h(z) = 1/f(z). So part (f) is about the reciprocal of a univalent function. They say: If h(z) = 1/z + c_0 + c_1 z + ... is injective on D and avoids the values z1 and z2, then |z1 - z2| ≤4. This matches: h avoids two values => f omits two values? Actually if h = 1/f, then h avoids 0 and 1/w? Wait: f avoids w => 1/f avoids 1/w and also avoids ∞? Actually 1/f avoids 0 because f never zero except at 0? But f(0)=0, so 1/f has a pole at 0, not a value. So h avoids two finite values corresponds to f omitting two points? Let's not get tangled; just follow hint.

We need to compute expansion of 1/(h(z)-z_j). Since h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + ... . Then h(z)-z_j = -z_j + 1/z + c_0 + c_1 z + ... . Write as (1/z)(1 - z_j z + c_0 z + c_1 z^2 + ...). Actually factor 1/z: h(z)-z_j = (1/z)[1 - z_j z + c_0 z + c_1 z^2 + c_2 z^3 + ...]. Then its reciprocal: 1/(h(z)-z_j) = z * [1 - z_j z + c_0 z + c_1 z^2 + ...]^{-1}. Expand using geometric series: = z * [1 + (z_j - c_0)z + ...]. Let's compute up to order z^2: Let A(z) = 1 - z_j z + c_0 z + c_1 z^2 + O(z^3) = 1 + (c_0 - z_j)z + c_1 z^2 + O(z^3). Then (A)^{-1} = 1 - (c_0 - z_j)z + [(c_0 - z_j)^2 - c_1]z^2 + O(z^3). Multiply by z: 1/(h(z)-z_j) = z - (c_0 - z_j)z^2 + [(c_0 - z_j)^2 - c_1]z^3 + O(z^4). But we need expansion in form 1/z + ...? Wait we expect a simple pole at 0 because h(z)-z_j has a simple pole at 0 (since h has pole 1/z). So its reciprocal should have a zero at 0? Actually h(z) has a simple pole at 0, so h(z)-z_j also has a simple pole at 0, thus its reciprocal has a simple zero at 0. So expansion should start with a term proportional to z, not 1/z. Indeed we got leading term z. So the expansion is of form A_1 z + A_2 z^2 + ... . But the problem statement says "Look at the second coefficient in the power series expansion of 1/(h(z)-z_j)". Perhaps they consider expansion around 0 after factoring out z? Or they consider the function (1/(h(z)-z_j))/z? Let's check typical proof: For univalent f(z)=z+ a_2 z^2+..., the function φ(z) = (f(z)-z_1)/(f(z)-z_2) maps D into C\{0,1}? Actually if f omits z1 and z2, then φ omits 0 and ∞? Not sure.

Alternatively, known result: If a univalent function omits two values, then the distance between them is at most 4. This is a corollary of Bieberbach's conjecture (now theorem) for the second coefficient. The proof: Suppose f omits w1 and w2. Consider g(z) = (f(z)-w1)/(f(z)-w2). Then g is analytic, maps D into C\{0}? Actually g omits 0 and ∞? Since f never equals w1 or w2, numerator and denominator never zero, so g is nonzero and finite, thus log g is analytic? Then we can get bound on derivative at 0 leading to |w1-w2| ≤ 2|a_2| ≤4. Something like that.

But the problem's hint: Look at second coefficient in power series expansion of 1/(h(z)-z_j). So they want to apply part (c) to the function 1/(h(z)-z_j) which has expansion 1/z + ...? Wait maybe they consider h(z) as having expansion 1/z + c_0 + c_1 z + ... (pole at 0). Then 1/(h(z)-z_j) will also have a simple pole at 0? Let's check: h(z) has a simple pole at 0 with residue 1. Subtracting constant z_j does not change the principal part: still 1/z + ... So h(z)-z_j also has a simple pole at 0 with residue 1. Therefore its reciprocal has a simple zero at 0, not a pole. So expansion starts with a_1 z + ... . So maybe they consider z/(h(z)-z_j) which would have expansion 1/z + ...? Actually z/(h(z)-z_j) = z * 1/(h(z)-z_j) would then have expansion starting with constant term? Let's compute: Since 1/(h(z)-z_j) = z - (c_0 - z_j)z^2 + ... then multiply by z gives z^2 - (c_0 - z_j)z^3 + ... still no 1/z term. Hmm.

Maybe they meant to consider the function 1/(h(z)-z_j) after a change of variable w=1/z? Not sure.

Let's look at part (f) statement: "If h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \cdots is injective on \mathbb{D} and avoids the values z_1 and z_2, show that |z_1 - z_2| \le 4." So h is of the form with a simple pole at 0, residue 1. It avoids two values. This is exactly the form of 1/f(z) where f is univalent normalized. Indeed if f(z)=z+ a_2 z^2+..., then 1/f(z) = 1/z - a_2 + (a_2^2 - a_3)z + ... So h(z) = 1/f(z). Then h avoids two values means 1/f avoids two values, i.e., f omits two points? Actually if h avoids value α, then 1/f(z) ≠ α => f(z) ≠ 1/α. So h avoids two values corresponds to f omitting two points (the reciprocals). So part (f) is essentially: If a univalent normalized f omits two values w1 and w2, then |1/w1 - 1/w2| ≤ 4? Wait we need to check.

Given h = 1/f, h avoids z1 and z2 => f avoids 1/z1 and 1/z2. Then the claim |z1 - z2| ≤ 4 becomes |1/w1 - 1/w2| ≤ 4 => |w2 - w1|/(|w1 w2|) ≤ 4. Not the standard result. So maybe they intend h itself to be univalent (injective) with a pole at 0, and we want to bound distance between two omitted values of h. This is a known result: For a univalent function on the punctured disc with expansion 1/z + ..., the omitted values lie in a disk of radius 2? Actually there is a theorem: If φ is univalent on {0<|z|<1} with φ(z)=1/z + b_0 + b_1 z + ..., then the omitted values lie in a disk of radius 2 centered at -b_0? Something like that. The distance between any two omitted values is at most 4. This is plausible.

Thus we need to prove: If h is injective on punctured disc, with expansion h(z)=1/z + c_0 + c_1 z + ..., and h omits two values z1, z2, then |z1 - z2| ≤ 4.

We can use part (c) applied to the function 1/(h(z)-z_j). Let's verify that 1/(h(z)-z_j) has expansion of the form 1/z + ...? Actually compute: h(z)-z_j = 1/z + (c_0 - z_j) + c_1 z + c_2 z^2 + ... . This still has a simple pole at 0 with residue 1. So its reciprocal has a simple zero at 0, not a pole. However, if we consider the function z/(h(z)-z_j) maybe? Let's compute: z/(h(z)-z_j) = z * 1/(h(z)-z_j). Since 1/(h(z)-z_j) = z - (c_0 - z_j)z^2 + ..., multiplying by z gives z^2 - (c_0 - z_j)z^3 + ... still no 1/z.

Alternatively, consider the function 1/(h(z)-z_j) after change of variable w=1/z? Let u=1/z, then near u=∞? Not helpful.

Maybe they meant to apply part (c) to the function h(z)-z_j? But h(z)-z_j has expansion 1/z + (c_0 - z_j) + c_1 z + ... which is of the form 1/z + d_0 + d_1 z + ... . Then part (c) applies to any function of that form that is injective on the punctured disc. Indeed h(z)-z_j is injective (since h is injective and subtracting constant doesn't affect injectivity) and has the same pole expansion. So we can apply part (c) to H_j(z) = h(z)-z_j. Then we get sum n|d_n|^2 ≤ 1 where d_n are coefficients of z^n in the regular part (i.e., d_0 = c_0 - z_j, d_1 = c_1, etc). So we get |c_1|^2 *1 ≤ 1? Actually sum n|d_n|^2 = 1*|d_1|^2 + 2*|d_2|^2 + ... ≤ 1. In particular |d_1| ≤ 1. So |c_1| ≤ 1. That gives a bound on c_1 independent of j. But we need to relate c_1 to z1 - z2. How does c_1 appear? Actually c_1 is the coefficient of z in h(z). It does not involve z_j. So we need another relation.

Maybe we consider the difference of the two functions 1/(h(z)-z1) and 1/(h(z)-z2). Their expansions will have different constant terms, and the difference will eliminate c_0 etc, leaving something proportional to (z1 - z2). Let's compute:

Let A_j(z) = 1/(h(z)-z_j). As we computed, A_j(z) = z - (c_0 - z_j)z^2 + ... . So the coefficient of z^2 in A_j is -(c_0 - z_j). Then the difference A_1(z) - A_2(z) = [-(c_0 - z_1) + (c_0 - z_2)] z^2 + ... = (z_1 - z_2) z^2 + higher order. So the coefficient of z^2 in the difference is (z_1 - z_2). Now note that A_j(z) are analytic on D (since h(z)-z_j never zero because h omits z_j). Moreover, A_j are injective? Not necessarily. But we can bound their derivatives at 0 using Schwarz lemma? Actually A_j(0)=0, A_j'(0)=1 (from expansion: A_j(z)= z + ...). So each A_j is a normalized analytic function (fixing 0 with derivative 1). If we also know they are injective? Let's check: If h is injective, does it imply that A_j(z)=1/(h(z)-z_j) is injective? Suppose A_j(z1)=A_j(z2). Then 1/(h(z1)-z_j)=1/(h(z2)-z_j) => h(z1)-z_j = h(z2)-z_j => h(z1)=h(z2) => z1=z2 by injectivity of h. So yes, A_j is injective as well. Good! So each A_j is injective on D, with A_j(0)=0, A_j'(0)=1. Then we can apply Bieberbach's coefficient bound (which we are proving) to A_j. But we are in the process of proving it; however part (e) gave bound on a_2 for normalized univalent functions. Actually we have proven up to part (e) that |a_2| ≤ 2 for normalized univalent f. That is exactly the Bieberbach bound for n=2. So we can use that result for A_j. Since A_j(z)=z + α_2 z^2 + ... where α_2 = -(c_0 - z_j). Then by part (e), |α_2| ≤ 2. Hence |c_0 - z_j| ≤ 2 for j=1,2. Then by triangle inequality, |z_1 - z_2| ≤ |z_1 - c_0| + |c_0 - z_2| ≤ 2+2 =4. That yields the desired bound. This matches the hint: "Look at the second coefficient in the power series expansion of 1/(h(z)-z_j)." Indeed the second coefficient (coefficient of z^2) is -(c_0 - z_j). So we use part (e) to bound it by 2.

Thus part (f) uses part (e). Good.

Now part (g): Complete the proof of Koebe-Bieberbach theorem: If f is injective normalized, then D_{1/4}(0) ⊂ f(D). Use contradiction: assume ∃ w with |w|<1/4 not in f(D). Then consider h=1/f. h is injective on punctured disc, has expansion 1/z - a_2 + ... . h omits 0 and 1/w? Actually f never equals w, so 1/f never equals 1/w. Also f(0)=0 => 1/f has a pole at 0, not a value. So h omits two values: 0 and 1/w. Apply part (f) to h: distance between omitted values ≤4 => |0 - 1/w| ≤4 => 1/|w| ≤4 => |w| ≥ 1/4, contradicting |w|<1/4. Hence no such w. The function f(z)=z/(1-z)^2 omits -1/4, showing sharpness.

Now we need to produce a full solution with detailed proofs for each part.

We must be careful about definitions: D = unit disc { |z|<1 }. D_r(0) = disc radius r.

We need to show (a) and (b) as given.

Part (c): Provide proof using area theorem (Gronwall's area theorem). We'll derive area of complement of h(D_ρ\{0}) = π(1/ρ^2 - Σ n|c_n|^2 ρ^{2n}). Provide justification: For a univalent function h on the punctured disc, the area of image of annulus? Actually area theorem: If f(z)=z + b_1 z^2 + ... is univalent on D, then Σ n|b_n|^2 ≤ 1. For a function with a pole, we consider g(z)=1/f(1/z) etc. But we can directly cite known area theorem for functions with a simple pole: If φ(z)=1/z + c_0 + c_1 z + ... is univalent on 0<|z|<1, then Σ n|c_n|^2 ≤ 1. Provide proof via considering the complement area.

We'll produce a rigorous argument: For 0<ρ<1, consider the domain Ω_ρ = h({ρ<|z|<1})? Actually the hint says: Calculate area of complement of h(D_ρ(0) - {0}) where 0<ρ<1, and let ρ→1. The set h(D_ρ\{0}) is the image of the punctured disc of radius ρ under h. Its complement in the extended complex plane? Actually we consider the area of the complement of h(D_ρ\{0}) in ℂ (maybe plus point at infinity). Since h has a pole at 0, as z→0, h(z)→∞, so the image of a small punctured neighbourhood of 0 is a neighbourhood of ∞. So the complement of h(D_ρ\{0}) is a bounded set (excluding ∞). Its area can be computed via integral formula: Area = ∬_{|z|>ρ} |h'(z)|^2 dA(z) (using change of variables). Then expand h'(z) in Laurent series and integrate termwise to get the expression.

We'll present that.

Part (d): Show existence of g. Need to argue f(z)/z is nowhere vanishing: Since f is injective and f(0)=0, f(z)≠0 for z≠0. Also f'(0)=1 ensures f(z)/z →1 as z→0, so it's nonzero in a neighbourhood; by injectivity, can't have zeros elsewhere. So we can define holomorphic logarithm and sqrt.

Then show g(z)=z ψ(z^2) is injective: Suppose g(z1)=g(z2). Then z1 ψ(z1^2)=z2 ψ(z2^2). Square both sides: z1^2 ψ(z1^2)^2 = z2^2 ψ(z2^2)^2 => f(z1^2)=f(z2^2). Since f is injective, z1^2=z2^2. So z1=±z2. But g is odd? Actually g(-z) = -z ψ((-z)^2) = -z ψ(z^2) = -g(z). So if z1=-z2, then g(z1) = -g(z2). For them to be equal, we need g(z1)=g(z2) => -g(z2)=g(z2) => g(z2)=0 => z2=0 => then z1=0. So injective.

Also g(0)=0, g'(0)=ψ(0)=1.

Part (e): Use expansion to bound a_2.

We need to compute ψ(z) = sqrt(f(z)/z). Since f(z)/z = 1 + a_2 z + a_3 z^2 + ... . Its sqrt: ψ(z) = 1 + (a_2/2) z + ... . Then g(z)=z ψ(z^2) = z (1 + (a_2/2) z^2 + ...) = z + (a_2/2) z^3 + ... . So b_2 = a_2/2.

Now 1/g(z) = 1/z - (a_2/2) z + ... . Apply part (c) to 1/g (which is of the form 1/z + ...). The coefficient of z is -a_2/2, so by (c) we get | -a_2/2| ≤ 1 => |a_2| ≤ 2.

Equality case: If |a_2|=2, then equality in (c) forces 1/g(z) = 1/z + λ z with |λ|=1. So -a_2/2 = λ => a_2 = -2λ. Then g(z) = z/(1+ λ z^2). Then f(z^2)=g(z)^2 = z^2/(1+ λ z^2)^2 => replace z^2 by w: f(w)= w/(1+ λ w)^2. Since λ = e^{iθ} for some θ, we get f(z)= z/(1+ e^{iθ} z)^2.

Part (f): As argued, define A_j(z)=1/(h(z)-z_j). Show A_j is injective, normalized (A_j(0)=0, A_j'(0)=1). Expand: A_j(z)= z - (c_0 - z_j) z^2 + ... . So the coefficient of z^2 is -(c_0 - z_j). By part (e), |-(c_0 - z_j)| ≤ 2 => |c_0 - z_j| ≤ 2. Then |z_1 - z_2| ≤ |z_1 - c_0| + |c_0 - z_2| ≤ 4.

Part (g): As described.

Now we need to write a full solution with clear steps, proofs, and justifications.

We'll produce a final answer with sections (a)-(g). Ensure we mention any theorems used (open mapping theorem, area theorem, etc.) and provide details.

Let's craft the solution.



---

## Model Solution

**Solution.**  
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and \(D_r(0)=\{z:|z|<r\}\).  
All functions are holomorphic on the indicated domains.

--------------------------------------------------------------------
### (a)  No uniform radius without extra hypotheses  

Take  

\[
f_n(z)=\frac{z}{n}\qquad (n\in\mathbb N).
\]

* \(f_n(0)=0\) and each \(f_n\) is holomorphic on \(\mathbb D\).  
* \(f_n(\mathbb D)=\{w:|w|<1/n\}=D_{1/n}(0)\); hence \(\displaystyle \frac1n\notin f_n(\mathbb D)\).  
* \(f_n'(z)=\frac1n\), so \(f_n'(0)=\frac1n\to0\).

If a number \(r>0\) worked for **every** holomorphic \(f\) with \(f(0)=0\), then in particular it would work for the \(f_n\).  
Choose \(n\) so large that \(\frac1n<r\). Then \(\frac1n\in D_r(0)\) but \(\frac1n\notin f_n(\mathbb D)\); thus \(D_r(0)\not\subset f_n(\mathbb D)\).  
Hence no such \(r\) exists.

--------------------------------------------------------------------
### (b)  The hypothesis \(f'(0)=1\) still does not give a uniform radius  

For \(\varepsilon>0\) set  

\[
f_\varepsilon(z)=\varepsilon\bigl(e^{z/\varepsilon}-1\bigr).
\]

* \(f_\varepsilon(0)=0\).  
* Differentiating, \(f_\varepsilon'(z)=e^{z/\varepsilon}\); hence \(f_\varepsilon'(0)=1\).  
* Since \(e^{z/\varepsilon}\neq0\) for all \(z\), we have \(f_\varepsilon(z)\neq-\varepsilon\); i.e. \(-\varepsilon\notin f_\varepsilon(\mathbb D)\).

Now let any \(r>0\) be given. Choose \(\varepsilon<r\). Then \(-\varepsilon\in D_r(0)\) but \(-\varepsilon\notin f_\varepsilon(\mathbb D)\); consequently \(D_r(0)\not\subset f_\varepsilon(\mathbb D)\).  
Thus even with the normalization \(f'(0)=1\) no universal \(r\) exists.

--------------------------------------------------------------------
### (c)  An area estimate for functions with a simple pole  

Let  

\[
h(z)=\frac1z+c_0+c_1z+c_2z^2+\cdots\qquad (0<|z|<1)
\]

be injective on the punctured disc.  
For \(0<\rho<1\) consider the image  

\[
h\bigl(D_\rho(0)\setminus\{0\}\bigr).
\]

Because \(h\) has a simple pole at \(0\) with residue \(1\), as \(|z|\to0\) we have \(h(z)\to\infty\); therefore the complement of this image in \(\mathbb C\) is a bounded set. Its area can be computed by the change‑of‑variables formula:

\[
\operatorname{Area}\bigl(\mathbb C\setminus h(D_\rho\setminus\{0\})\bigr)
   =\iint_{|z|>\rho}|h'(z)|^{2}\,dA(z),
\]
where \(dA\) denotes Euclidean area element.

Write the Laurent series of \(h'\):

\[
h'(z)=-\frac1{z^{2}}+c_1+2c_2z+3c_3z^{2}+\cdots .
\]

Hence  

\[
|h'(z)|^{2}
   =\frac1{|z|^{4}}
     -2\operatorname{Re}\!\Bigl(\frac{\overline{c_1}}{z^{2}}\Bigr)
     +\sum_{n\ge1}n^{2}|c_n|^{2}|z|^{2n-2}
     +\text{terms integrating to zero over circles}.
\]

Integrating over the annulus \(\rho<|z|<\infty\) and using  
\(\displaystyle\int_{\rho}^{2\pi}\!\! r^{k}\,d\theta\,dr=
   \begin{cases}
   2\pi\frac{\rho^{k+2}}{k+2}, & k\neq-2,\\[2pt]
   -2\pi\log\rho, & k=-2,
   \end{cases}\)
we obtain  

\[
\operatorname{Area}\bigl(\mathbb C\setminus h(D_\rho\setminus\{0\})\bigr)
   =\pi\Bigl(\frac1{\rho^{2}}-\sum_{n\ge1}n|c_n|^{2}\rho^{2n}\Bigr).
\]

Since an area is non‑negative,  

\[
\sum_{n\ge1}n|c_n|^{2}\rho^{2n}\le\frac1{\rho^{2}}\qquad(0<\rho<1).
\]

Letting \(\rho\to1^{-}\) (the left–hand side increases with \(\rho\)) gives  

\[
\boxed{\displaystyle\sum_{n\ge1}n|c_n|^{2}\le1}.
\]

This is Gronwall’s area theorem for functions with a simple pole.

--------------------------------------------------------------------
### (d)  Constructing the square‑root function  

Let  

\[
f(z)=z+a_2z^{2}+a_3z^{3}+\cdots
\]

be injective on \(\mathbb D\) with \(f(0)=0,\;f'(0)=1\).

*Because \(f\) is injective and \(f(0)=0\), we have \(f(z)\neq0\) for \(z\neq0\).*  
Moreover  

\[
\frac{f(z)}{z}=1+a_2z+a_3z^{2}+\cdots
\]

is holomorphic on \(\mathbb D\) and equals \(1\) at \(0\); hence it never vanishes.  
Since \(\mathbb D\) is simply connected, there exists a holomorphic function \(\psi\) on \(\mathbb D\) such that  

\[
\psi(z)^{2}= \frac{f(z)}{z},\qquad \psi(0)=1 .
\]

Define  

\[
g(z)=z\,\psi(z^{2}).
\]

Then  

\[
g(z)^{2}=z^{2}\psi(z^{2})^{2}=z^{2}\frac{f(z^{2})}{z^{2}}=f(z^{2}),
\]
so \(g^{2}(z)=f(z^{2})\).

*Injectivity of \(g\).*  
If \(g(z_{1})=g(z_{2})\) then squaring gives \(f(z_{1}^{2})=f(z_{2}^{2})\); injectivity of \(f\) yields \(z_{1}^{2}=z_{2}^{2}\), i.e. \(z_{1}=\pm z_{2}\).  
But \(g\) is odd: \(g(-z)=-z\psi(z^{2})=-g(z)\).  
Hence \(z_{1}=-z_{2}\) would imply \(g(z_{1})=-g(z_{2})\); equality forces \(g(z_{2})=0\), which only happens at \(z_{2}=0\) (because \(g'(0)=1\neq0\)). Thus \(z_{1}=z_{2}\).  

Finally, \(g(0)=0\) and  

\[
g'(z)=\psi(z^{2})+2z^{2}\psi'(z^{2})\;\Longrightarrow\;g'(0)=\psi(0)=1 .
\]

Thus \(g\) satisfies the same hypotheses as \(f\).

--------------------------------------------------------------------
### (e)  The second coefficient bound  

From the construction in (d),

\[
\psi(z)=\sqrt{\frac{f(z)}{z}}
      =1+\frac{a_{2}}{2}z+\Bigl(\frac{a_{3}}{2}-\frac{a_{2}^{2}}{8}\Bigr)z^{2}+\cdots .
\]

Hence  

\[
g(z)=z\psi(z^{2})
    =z\Bigl(1+\frac{a_{2}}{2}z^{2}+O(z^{4})\Bigr)
    =z+\frac{a_{2}}{2}z^{3}+O(z^{5}),
\]
so the power series of \(g\) is  

\[
g(z)=z+b_{2}z^{3}+b_{4}z^{5}+\cdots ,\qquad b_{2}=\frac{a_{2}}{2}.
\]

Consequently  

\[
\frac{1}{g(z)}=\frac1z-b_{2}z+O(z^{3})
            =\frac1z-\frac{a_{2}}{2}z+O(z^{3}).
\]

The function \(1/g\) is of the form required in part (c): it is injective on \(\mathbb D\) (because \(g\) is) and has a simple pole at \(0\) with residue \(1\).  
Applying the estimate of part (c) to \(1/g\) gives  

\[
\bigl|-\tfrac{a_{2}}{2}\bigr|^{2}\le 1\quad\Longrightarrow\quad |a_{2}|\le 2 .
\]

*Equality case.*  
If \(|a_{2}|=2\), then equality holds in the area theorem, which forces the function to have exactly two non‑zero coefficients:

\[
\frac{1}{g(z)}=\frac1z+\lambda z\qquad\text{with }|\lambda|=1 .
\]

Thus \(-\frac{a_{2}}{2}=\lambda\), i.e. \(a_{2}=-2\lambda\).  
From \(\frac{1}{g(z)}=\frac1z+\lambda z\) we obtain  

\[
g(z)=\frac{z}{1+\lambda z^{2}} .
\]

Now \(f(z^{2})=g(z)^{2}= \dfrac{z^{2}}{(1+\lambda z^{2})^{2}}\).  
Replacing \(z^{2}\) by \(w\) yields  

\[
f(w)=\frac{w}{(1+\lambda w)^{2}},\qquad \lambda=e^{i\theta}\;(\theta\in\mathbb R).
\]

Hence the extremal functions are precisely the rotations of the Koebe function  

\[
f(z)=\frac{z}{(1-e^{i\theta}z)^{2}} .
\]

--------------------------------------------------------------------
### (f)  Distance between two omitted values  

Let  

\[
h(z)=\frac1z+c_{0}+c_{1}z+c_{2}z^{2}+\cdots
\]

be injective on \(\mathbb D\) and assume that \(h\) omits the two distinct values \(z_{1},z_{2}\).  
For \(j=1,2\) set  

\[
H_{j}(z)=\frac{1}{h(z)-z_{j}} .
\]

Because \(h\) never equals \(z_{j}\), each \(H_{j}\) is holomorphic on \(\mathbb D\).  
If \(H_{j}(u)=H_{j}(v)\) then \(h(u)-z_{j}=h(v)-z_{j}\), so \(h(u)=h(v)\); injectivity of \(h\) gives \(u=v\). Thus each \(H_{j}\) is injective.

Moreover, \(h(z)-z_{j}\) has the same principal part as \(h(z)\), namely \(1/z\); consequently  

\[
H_{j}(0)=0,\qquad H_{j}'(0)=1 .
\]

Expanding \(h(z)-z_{j}\) we obtain  

\[
h(z)-z_{j}= \frac1z+(c_{0}-z_{j})+c_{1}z+c_{2}z^{2}+\cdots ,
\]
and therefore  

\[
H_{j}(z)=z-(c_{0}-z_{j})z^{2}+O(z^{3}).
\]

Thus the coefficient of \(z^{2}\) in the power series of \(H_{j}\) is \(-(c_{0}-z_{j})\).

By part (e) applied to the injective function \(H_{j}\) (which is of the form \(z+\alpha_{2}z^{2}+\cdots\) with \(\alpha_{2}=-(c_{0}-z_{j})\)) we have  

\[
|-(c_{0}-z_{j})|\le 2\quad\Longrightarrow\quad |c_{0}-z_{j}|\le 2\qquad(j=1,2).
\]

Finally,

\[
|z_{1}-z_{2}|
   \le |z_{1}-c_{0}|+|c_{0}-z_{j}|
   \le 2+2=4 .
\]

Hence  

\[
\boxed{|z_{1}-z_{2}|\le 4}.
\]

--------------------------------------------------------------------
### (g)  Completion of the Koebe–Bieberbach theorem  

Let \(f\) be injective on \(\mathbb D\) with \(f(0)=0,\;f'(0)=1\).  
Write its Taylor expansion  

\[
f(z)=z+a_{2}z^{2}+a_{3}z^{3}+\cdots .
\]

Assume, for a contradiction, that there exists a number \(w\) with  

\[
0<|w|<\frac14\qquad\text{and}\qquad w\notin f(\mathbb D).
\]

Consider the reciprocal  

\[
h(z)=\frac{1}{f(z)} .
\]

Because \(f\) is injective and \(f(0)=0\), the function \(h\) is injective on the punctured disc \(0<|z|<1\); it has a simple pole at \(0\) with residue \(1\), so  

\[
h(z)=\frac1z - a_{2}+ (a_{2}^{2}-a_{3})z+\cdots .
\]

Since \(f\) never takes the value \(w\), the function \(h\) never takes the value \(1/w\); moreover \(h(z)\neq0\) for \(z\neq0\) (because \(f(z)\neq0\) there). Thus \(h\) omits the two distinct values \(0\) and \(1/w\).

Applying part (f) to \(h\) we obtain  

\[
\bigl|0-\tfrac1w\bigr|\le 4\quad\Longrightarrow\quad \frac1{|w|}\le 4\quad\Longrightarrow\quad |w|\ge\frac14 .
\]

This contradicts the choice \(|w|<\frac14\). Hence no such \(w\) exists; i.e.

\[
D_{1/4}(0)\subseteq f(\mathbb D).
\]

The bound is sharp: the Koebe function  

\[
k(z)=\frac{z}{(1-z)^{2}}=z+2z^{2}+3z^{3}+\cdots
\]

satisfies \(k(0)=0,\;k'(0)=1\) and is injective on \(\mathbb D\), yet  

\[
k(\mathbb D)=\mathbb C\setminus\bigl(-\infty,-\tfrac14\bigr],
\]
so \(-1/4\notin k(\mathbb D)\). Thus no larger radius than \(1/4\) can work for all normalized univalent functions.

--------------------------------------------------------------------
**Conclusion.**  
We have proved:

* (a) Without extra hypotheses no uniform radius exists.  
* (b) Even with the normalization \(f'(0)=1\) no uniform radius exists.  
* (c) For a function \(h(z)=1/z+c_{0}+c_{1}z+\cdots\) injective on the punctured disc, \(\sum n|c_{n}|^{2}\le1\).  
* (d) From a normalized univalent \(f\) we can construct another normalized univalent \(g\) with \(g^{2}(z)=f(z^{2})\).  
* (e) Consequently \(|a_{2}|\le2\), with equality exactly for the rotations of the Koebe function \(z/(1-e^{i\theta}z)^{2}\).  
* (f) If an injective function of the form \(1/z+\cdots\) omits two values, their distance is at most \(4\).  
* (g) Using (f) applied to \(1/f\) we obtain the Koebe–Bieberbach theorem: every normalized univalent function maps \(\mathbb D\) onto a domain containing the disc of radius \(1/4\), and this radius is best possible.

Thus the theorem is established. ∎

---

## Reasoning Details (raw)

```json
[
  {
    "type": "reasoning.text",
    "text": "We need to produce a full solution with proofs for each part (a)-(g). The problem statement is given. The solution skeleton is provided in the prompt but we need to flesh out details, ensure rigorous proofs, correct any mistakes, and present a clean solution.\n\nWe need to show:\n\n(a) No uniform r exists without further restrictions: Provide sequence f_n(z)=z/n, show f_n'(0)=1/n \u21920, and 1/n not in image.\n\n(b) Even with f'(0)=1, no uniform r: Use f_\u03b5(z)=\u03b5(e^{z/\u03b5} -1). Show f_\u03b5(0)=0, f_\u03b5'(0)=1, image omits -\u03b5, so for any r>0 choose \u03b5<r then -\u03b5\u2208D_r(0) not in image.\n\n(c) For h(z)=1/z + c_0 + c_1 z + ... injective on punctured disc, prove sum n|c_n|^2 \u22641. Use area theorem (Gronwall's area theorem). Compute area of complement of h(D_\u03c1\\{0}) as \u03c0(1/\u03c1^2 - \u03a3 n|c_n|^2 \u03c1^{2n})\u22650. Then let \u03c1\u21921.\n\n(d) Given f(z)=z+ a_2 z^2+... injective with f(0)=0, f'(0)=1, construct g such that g^2(z)=f(z^2). Show f(z)/z nowhere vanishing, define \u03c8 holomorphic sqrt with \u03c8(0)=1, set g(z)=z \u03c8(z^2). Show g injective, g(0)=0, g'(0)=1.\n\n(e) Using (c) on 1/g, bound |a_2|\u22642, equality case yields Koebe function. Need to compute expansion: g(z)=z + b_2 z^3+..., then 1/g(z)=1/z - b_2 z +..., apply (c) to get |b_2|\u22641, thus |a_2|=2|b_2|\u22642. Equality forces 1/g(z)=1/z + e^{i\u03b8} z, thus g(z)=z/(1+ e^{i\u03b8}z^2). Then f(z)=z/(1+ e^{i\u03b8}z)^2.\n\n(f) If h injective on disc and avoids two values z1,z2, then |z1 - z2| \u22644. Consider functions 1/(h(z)-z_j) which are injective with simple pole at 0. Expand: 1/(h(z)-z_j)=1/z + \u03b1_{0j}+ \u03b1_{1j} z+... Apply (c) to get |\u03b1_{1j}|\u22641. Then relate \u03b1_{1j} to z_j: compute expansion: Since h(z)=z+ a_2 z^2+..., then h(z)-z_j = -z_j + z + a_2 z^2+...; its reciprocal expansion yields coefficient of z equals something like (1+z_j^2?) Actually need to derive correctly. Standard proof: For univalent f(z)=z+ a_2 z^2+..., the function 1/f(z) = 1/z - a_2 + ...? Wait compute: f(z)=z+ a_2 z^2+ a_3 z^3+... Then 1/f(z) = (1/z) * 1/(1+ a_2 z+ a_3 z^2+...) = (1/z)(1 - a_2 z + (a_2^2 - a_3) z^2+...). So 1/f(z) = 1/z - a_2 + (a_2^2 - a_3) z + ... So coefficient of z is a_2^2 - a_3. Not directly a_2. However for the function 1/(f(z)-w) we can get linear term related to w. There's known inequality: |z1 - z2| \u2264 4 for omitted values of a univalent function normalized f(0)=0, f'(0)=1. This is a corollary of Bieberbach's coefficient bound |a_2| \u22642. Actually the proof: If f omits w1 and w2, then consider g(z)= (f(z)-w1)/(f(z)-w2) which maps disc into disc omitting 0 and \u221e? Hmm.\n\nBut the problem's hint: Look at second coefficient in power series expansion of 1/(h(z)-z_j). So they want to compute expansion of 1/(h(z)-z_j) = 1/z + c_0 + c_1 z + ... and relate c_1 to z_j. Let's derive.\n\nLet h(z) be injective on D, with h(0)=0, h'(0)=1? Actually part (f) says: If h(z) = 1/z + c_0 + c_1 z + ... is injective on D and avoids the values z1 and z2, show |z1 - z2| \u22644. Wait they defined h(z) as having a pole at 0 (like 1/z + ...). That's the form of 1/f(z) after normalization? Actually if f is univalent normalized, then 1/f(z) has a simple pole at 0 with residue 1, expansion 1/z - a_2 + ... So indeed h(z) = 1/f(z). So part (f) is about the reciprocal of a univalent function. They say: If h(z) = 1/z + c_0 + c_1 z + ... is injective on D and avoids the values z1 and z2, then |z1 - z2| \u22644. This matches: h avoids two values => f omits two values? Actually if h = 1/f, then h avoids 0 and 1/w? Wait: f avoids w => 1/f avoids 1/w and also avoids \u221e? Actually 1/f avoids 0 because f never zero except at 0? But f(0)=0, so 1/f has a pole at 0, not a value. So h avoids two finite values corresponds to f omitting two points? Let's not get tangled; just follow hint.\n\nWe need to compute expansion of 1/(h(z)-z_j). Since h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + ... . Then h(z)-z_j = -z_j + 1/z + c_0 + c_1 z + ... . Write as (1/z)(1 - z_j z + c_0 z + c_1 z^2 + ...). Actually factor 1/z: h(z)-z_j = (1/z)[1 - z_j z + c_0 z + c_1 z^2 + c_2 z^3 + ...]. Then its reciprocal: 1/(h(z)-z_j) = z * [1 - z_j z + c_0 z + c_1 z^2 + ...]^{-1}. Expand using geometric series: = z * [1 + (z_j - c_0)z + ...]. Let's compute up to order z^2: Let A(z) = 1 - z_j z + c_0 z + c_1 z^2 + O(z^3) = 1 + (c_0 - z_j)z + c_1 z^2 + O(z^3). Then (A)^{-1} = 1 - (c_0 - z_j)z + [(c_0 - z_j)^2 - c_1]z^2 + O(z^3). Multiply by z: 1/(h(z)-z_j) = z - (c_0 - z_j)z^2 + [(c_0 - z_j)^2 - c_1]z^3 + O(z^4). But we need expansion in form 1/z + ...? Wait we expect a simple pole at 0 because h(z)-z_j has a simple pole at 0 (since h has pole 1/z). So its reciprocal should have a zero at 0? Actually h(z) has a simple pole at 0, so h(z)-z_j also has a simple pole at 0, thus its reciprocal has a simple zero at 0. So expansion should start with a term proportional to z, not 1/z. Indeed we got leading term z. So the expansion is of form A_1 z + A_2 z^2 + ... . But the problem statement says \"Look at the second coefficient in the power series expansion of 1/(h(z)-z_j)\". Perhaps they consider expansion around 0 after factoring out z? Or they consider the function (1/(h(z)-z_j))/z? Let's check typical proof: For univalent f(z)=z+ a_2 z^2+..., the function \u03c6(z) = (f(z)-z_1)/(f(z)-z_2) maps D into C\\{0,1}? Actually if f omits z1 and z2, then \u03c6 omits 0 and \u221e? Not sure.\n\nAlternatively, known result: If a univalent function omits two values, then the distance between them is at most 4. This is a corollary of Bieberbach's conjecture (now theorem) for the second coefficient. The proof: Suppose f omits w1 and w2. Consider g(z) = (f(z)-w1)/(f(z)-w2). Then g is analytic, maps D into C\\{0}? Actually g omits 0 and \u221e? Since f never equals w1 or w2, numerator and denominator never zero, so g is nonzero and finite, thus log g is analytic? Then we can get bound on derivative at 0 leading to |w1-w2| \u2264 2|a_2| \u22644. Something like that.\n\nBut the problem's hint: Look at second coefficient in power series expansion of 1/(h(z)-z_j). So they want to apply part (c) to the function 1/(h(z)-z_j) which has expansion 1/z + ...? Wait maybe they consider h(z) as having expansion 1/z + c_0 + c_1 z + ... (pole at 0). Then 1/(h(z)-z_j) will also have a simple pole at 0? Let's check: h(z) has a simple pole at 0 with residue 1. Subtracting constant z_j does not change the principal part: still 1/z + ... So h(z)-z_j also has a simple pole at 0 with residue 1. Therefore its reciprocal has a simple zero at 0, not a pole. So expansion starts with a_1 z + ... . So maybe they consider z/(h(z)-z_j) which would have expansion 1/z + ...? Actually z/(h(z)-z_j) = z * 1/(h(z)-z_j) would then have expansion starting with constant term? Let's compute: Since 1/(h(z)-z_j) = z - (c_0 - z_j)z^2 + ... then multiply by z gives z^2 - (c_0 - z_j)z^3 + ... still no 1/z term. Hmm.\n\nMaybe they meant to consider the function 1/(h(z)-z_j) after a change of variable w=1/z? Not sure.\n\nLet's look at part (f) statement: \"If h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \\cdots is injective on \\mathbb{D} and avoids the values z_1 and z_2, show that |z_1 - z_2| \\le 4.\" So h is of the form with a simple pole at 0, residue 1. It avoids two values. This is exactly the form of 1/f(z) where f is univalent normalized. Indeed if f(z)=z+ a_2 z^2+..., then 1/f(z) = 1/z - a_2 + (a_2^2 - a_3)z + ... So h(z) = 1/f(z). Then h avoids two values means 1/f avoids two values, i.e., f omits two points? Actually if h avoids value \u03b1, then 1/f(z) \u2260 \u03b1 => f(z) \u2260 1/\u03b1. So h avoids two values corresponds to f omitting two points (the reciprocals). So part (f) is essentially: If a univalent normalized f omits two values w1 and w2, then |1/w1 - 1/w2| \u2264 4? Wait we need to check.\n\nGiven h = 1/f, h avoids z1 and z2 => f avoids 1/z1 and 1/z2. Then the claim |z1 - z2| \u2264 4 becomes |1/w1 - 1/w2| \u2264 4 => |w2 - w1|/(|w1 w2|) \u2264 4. Not the standard result. So maybe they intend h itself to be univalent (injective) with a pole at 0, and we want to bound distance between two omitted values of h. This is a known result: For a univalent function on the punctured disc with expansion 1/z + ..., the omitted values lie in a disk of radius 2? Actually there is a theorem: If \u03c6 is univalent on {0<|z|<1} with \u03c6(z)=1/z + b_0 + b_1 z + ..., then the omitted values lie in a disk of radius 2 centered at -b_0? Something like that. The distance between any two omitted values is at most 4. This is plausible.\n\nThus we need to prove: If h is injective on punctured disc, with expansion h(z)=1/z + c_0 + c_1 z + ..., and h omits two values z1, z2, then |z1 - z2| \u2264 4.\n\nWe can use part (c) applied to the function 1/(h(z)-z_j). Let's verify that 1/(h(z)-z_j) has expansion of the form 1/z + ...? Actually compute: h(z)-z_j = 1/z + (c_0 - z_j) + c_1 z + c_2 z^2 + ... . This still has a simple pole at 0 with residue 1. So its reciprocal has a simple zero at 0, not a pole. However, if we consider the function z/(h(z)-z_j) maybe? Let's compute: z/(h(z)-z_j) = z * 1/(h(z)-z_j). Since 1/(h(z)-z_j) = z - (c_0 - z_j)z^2 + ..., multiplying by z gives z^2 - (c_0 - z_j)z^3 + ... still no 1/z.\n\nAlternatively, consider the function 1/(h(z)-z_j) after change of variable w=1/z? Let u=1/z, then near u=\u221e? Not helpful.\n\nMaybe they meant to apply part (c) to the function h(z)-z_j? But h(z)-z_j has expansion 1/z + (c_0 - z_j) + c_1 z + ... which is of the form 1/z + d_0 + d_1 z + ... . Then part (c) applies to any function of that form that is injective on the punctured disc. Indeed h(z)-z_j is injective (since h is injective and subtracting constant doesn't affect injectivity) and has the same pole expansion. So we can apply part (c) to H_j(z) = h(z)-z_j. Then we get sum n|d_n|^2 \u2264 1 where d_n are coefficients of z^n in the regular part (i.e., d_0 = c_0 - z_j, d_1 = c_1, etc). So we get |c_1|^2 *1 \u2264 1? Actually sum n|d_n|^2 = 1*|d_1|^2 + 2*|d_2|^2 + ... \u2264 1. In particular |d_1| \u2264 1. So |c_1| \u2264 1. That gives a bound on c_1 independent of j. But we need to relate c_1 to z1 - z2. How does c_1 appear? Actually c_1 is the coefficient of z in h(z). It does not involve z_j. So we need another relation.\n\nMaybe we consider the difference of the two functions 1/(h(z)-z1) and 1/(h(z)-z2). Their expansions will have different constant terms, and the difference will eliminate c_0 etc, leaving something proportional to (z1 - z2). Let's compute:\n\nLet A_j(z) = 1/(h(z)-z_j). As we computed, A_j(z) = z - (c_0 - z_j)z^2 + ... . So the coefficient of z^2 in A_j is -(c_0 - z_j). Then the difference A_1(z) - A_2(z) = [-(c_0 - z_1) + (c_0 - z_2)] z^2 + ... = (z_1 - z_2) z^2 + higher order. So the coefficient of z^2 in the difference is (z_1 - z_2). Now note that A_j(z) are analytic on D (since h(z)-z_j never zero because h omits z_j). Moreover, A_j are injective? Not necessarily. But we can bound their derivatives at 0 using Schwarz lemma? Actually A_j(0)=0, A_j'(0)=1 (from expansion: A_j(z)= z + ...). So each A_j is a normalized analytic function (fixing 0 with derivative 1). If we also know they are injective? Let's check: If h is injective, does it imply that A_j(z)=1/(h(z)-z_j) is injective? Suppose A_j(z1)=A_j(z2). Then 1/(h(z1)-z_j)=1/(h(z2)-z_j) => h(z1)-z_j = h(z2)-z_j => h(z1)=h(z2) => z1=z2 by injectivity of h. So yes, A_j is injective as well. Good! So each A_j is injective on D, with A_j(0)=0, A_j'(0)=1. Then we can apply Bieberbach's coefficient bound (which we are proving) to A_j. But we are in the process of proving it; however part (e) gave bound on a_2 for normalized univalent functions. Actually we have proven up to part (e) that |a_2| \u2264 2 for normalized univalent f. That is exactly the Bieberbach bound for n=2. So we can use that result for A_j. Since A_j(z)=z + \u03b1_2 z^2 + ... where \u03b1_2 = -(c_0 - z_j). Then by part (e), |\u03b1_2| \u2264 2. Hence |c_0 - z_j| \u2264 2 for j=1,2. Then by triangle inequality, |z_1 - z_2| \u2264 |z_1 - c_0| + |c_0 - z_2| \u2264 2+2 =4. That yields the desired bound. This matches the hint: \"Look at the second coefficient in the power series expansion of 1/(h(z)-z_j).\" Indeed the second coefficient (coefficient of z^2) is -(c_0 - z_j). So we use part (e) to bound it by 2.\n\nThus part (f) uses part (e). Good.\n\nNow part (g): Complete the proof of Koebe-Bieberbach theorem: If f is injective normalized, then D_{1/4}(0) \u2282 f(D). Use contradiction: assume \u2203 w with |w|<1/4 not in f(D). Then consider h=1/f. h is injective on punctured disc, has expansion 1/z - a_2 + ... . h omits 0 and 1/w? Actually f never equals w, so 1/f never equals 1/w. Also f(0)=0 => 1/f has a pole at 0, not a value. So h omits two values: 0 and 1/w. Apply part (f) to h: distance between omitted values \u22644 => |0 - 1/w| \u22644 => 1/|w| \u22644 => |w| \u2265 1/4, contradicting |w|<1/4. Hence no such w. The function f(z)=z/(1-z)^2 omits -1/4, showing sharpness.\n\nNow we need to produce a full solution with detailed proofs for each part.\n\nWe must be careful about definitions: D = unit disc { |z|<1 }. D_r(0) = disc radius r.\n\nWe need to show (a) and (b) as given.\n\nPart (c): Provide proof using area theorem (Gronwall's area theorem). We'll derive area of complement of h(D_\u03c1\\{0}) = \u03c0(1/\u03c1^2 - \u03a3 n|c_n|^2 \u03c1^{2n}). Provide justification: For a univalent function h on the punctured disc, the area of image of annulus? Actually area theorem: If f(z)=z + b_1 z^2 + ... is univalent on D, then \u03a3 n|b_n|^2 \u2264 1. For a function with a pole, we consider g(z)=1/f(1/z) etc. But we can directly cite known area theorem for functions with a simple pole: If \u03c6(z)=1/z + c_0 + c_1 z + ... is univalent on 0<|z|<1, then \u03a3 n|c_n|^2 \u2264 1. Provide proof via considering the complement area.\n\nWe'll produce a rigorous argument: For 0<\u03c1<1, consider the domain \u03a9_\u03c1 = h({\u03c1<|z|<1})? Actually the hint says: Calculate area of complement of h(D_\u03c1(0) - {0}) where 0<\u03c1<1, and let \u03c1\u21921. The set h(D_\u03c1\\{0}) is the image of the punctured disc of radius \u03c1 under h. Its complement in the extended complex plane? Actually we consider the area of the complement of h(D_\u03c1\\{0}) in \u2102 (maybe plus point at infinity). Since h has a pole at 0, as z\u21920, h(z)\u2192\u221e, so the image of a small punctured neighbourhood of 0 is a neighbourhood of \u221e. So the complement of h(D_\u03c1\\{0}) is a bounded set (excluding \u221e). Its area can be computed via integral formula: Area = \u222c_{|z|>\u03c1} |h'(z)|^2 dA(z) (using change of variables). Then expand h'(z) in Laurent series and integrate termwise to get the expression.\n\nWe'll present that.\n\nPart (d): Show existence of g. Need to argue f(z)/z is nowhere vanishing: Since f is injective and f(0)=0, f(z)\u22600 for z\u22600. Also f'(0)=1 ensures f(z)/z \u21921 as z\u21920, so it's nonzero in a neighbourhood; by injectivity, can't have zeros elsewhere. So we can define holomorphic logarithm and sqrt.\n\nThen show g(z)=z \u03c8(z^2) is injective: Suppose g(z1)=g(z2). Then z1 \u03c8(z1^2)=z2 \u03c8(z2^2). Square both sides: z1^2 \u03c8(z1^2)^2 = z2^2 \u03c8(z2^2)^2 => f(z1^2)=f(z2^2). Since f is injective, z1^2=z2^2. So z1=\u00b1z2. But g is odd? Actually g(-z) = -z \u03c8((-z)^2) = -z \u03c8(z^2) = -g(z). So if z1=-z2, then g(z1) = -g(z2). For them to be equal, we need g(z1)=g(z2) => -g(z2)=g(z2) => g(z2)=0 => z2=0 => then z1=0. So injective.\n\nAlso g(0)=0, g'(0)=\u03c8(0)=1.\n\nPart (e): Use expansion to bound a_2.\n\nWe need to compute \u03c8(z) = sqrt(f(z)/z). Since f(z)/z = 1 + a_2 z + a_3 z^2 + ... . Its sqrt: \u03c8(z) = 1 + (a_2/2) z + ... . Then g(z)=z \u03c8(z^2) = z (1 + (a_2/2) z^2 + ...) = z + (a_2/2) z^3 + ... . So b_2 = a_2/2.\n\nNow 1/g(z) = 1/z - (a_2/2) z + ... . Apply part (c) to 1/g (which is of the form 1/z + ...). The coefficient of z is -a_2/2, so by (c) we get | -a_2/2| \u2264 1 => |a_2| \u2264 2.\n\nEquality case: If |a_2|=2, then equality in (c) forces 1/g(z) = 1/z + \u03bb z with |\u03bb|=1. So -a_2/2 = \u03bb => a_2 = -2\u03bb. Then g(z) = z/(1+ \u03bb z^2). Then f(z^2)=g(z)^2 = z^2/(1+ \u03bb z^2)^2 => replace z^2 by w: f(w)= w/(1+ \u03bb w)^2. Since \u03bb = e^{i\u03b8} for some \u03b8, we get f(z)= z/(1+ e^{i\u03b8} z)^2.\n\nPart (f): As argued, define A_j(z)=1/(h(z)-z_j). Show A_j is injective, normalized (A_j(0)=0, A_j'(0)=1). Expand: A_j(z)= z - (c_0 - z_j) z^2 + ... . So the coefficient of z^2 is -(c_0 - z_j). By part (e), |-(c_0 - z_j)| \u2264 2 => |c_0 - z_j| \u2264 2. Then |z_1 - z_2| \u2264 |z_1 - c_0| + |c_0 - z_2| \u2264 4.\n\nPart (g): As described.\n\nNow we need to write a full solution with clear steps, proofs, and justifications.\n\nWe'll produce a final answer with sections (a)-(g). Ensure we mention any theorems used (open mapping theorem, area theorem, etc.) and provide details.\n\nLet's craft the solution.\n\n",
    "format": "unknown",
    "index": 0
  }
]
```

---

## Raw Response (truncated)

```json
{
  "id": "gen-1789204948-e96Tsn80gaJzthnP5gEh",
  "object": "chat.completion",
  "created": 1789204948,
  "model": "nvidia/nemotron-3-super-120b-a12b:free",
  "provider": "Nvidia",
  "system_fingerprint": null,
  "service_tier": null,
  "choices": [
    {
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop",
      "native_finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "**Solution.**  \nLet \\(\\mathbb D=\\{z\\in\\mathbb C:|z|<1\\}\\) and \\(D_r(0)=\\{z:|z|<r\\}\\).  \nAll functions are holomorphic on the indicated domains.\n\n--------------------------------------------------------------------\n### (a)  No uniform radius without extra hypotheses  \n\nTake  \n\n\\[\nf_n(z)=\\frac{z}{n}\\qquad (n\\in\\mathbb N).\n\\]\n\n* \\(f_n(0)=0\\) and each \\(f_n\\) is holomorphic on \\(\\mathbb D\\).  \n* \\(f_n(\\mathbb D)=\\{w:|w|<1/n\\}=D_{1/n}(0)\\); hence \\(\\displaystyle \\frac1n\\notin f_n(\\mathbb D)\\).  \n* \\(f_n'(z)=\\frac1n\\), so \\(f_n'(0)=\\frac1n\\to0\\).\n\nIf a number \\(r>0\\) worked for **every** holomorphic \\(f\\) with \\(f(0)=0\\), then in particular it would work for the \\(f_n\\).  \nChoose \\(n\\) so large that \\(\\frac1n<r\\). Then \\(\\frac1n\\in D_r(0)\\) but \\(\\frac1n\\notin f_n(\\mathbb D)\\); thus \\(D_r(0)\\not\\subset f_n(\\mathbb D)\\).  \nHence no such \\(r\\) exists.\n\n--------------------------------------------------------------------\n### (b)  The hypothesis \\(f'(0)=1\\) still does not give a uniform radius  \n\nFor \\(\\varepsilon>0\\) set  \n\n\\[\nf_\\varepsilon(z)=\\varepsilon\\bigl(e^{z/\\varepsilon}-1\\bigr).\n\\]\n\n* \\(f_\\varepsilon(0)=0\\).  \n* Differentiating, \\(f_\\varepsilon'(z)=e^{z/\\varepsilon}\\); hence \\(f_\\varepsilon'(0)=1\\).  \n* Since \\(e^{z/\\varepsilon}\\neq0\\) for all \\(z\\), we have \\(f_\\varepsilon(z)\\neq-\\varepsilon\\); i.e. \\(-\\varepsilon\\notin f_\\varepsilon(\\mathbb D)\\).\n\nNow let any \\(r>0\\) be given. Choose \\(\\varepsilon<r\\). Then \\(-\\varepsilon\\in D_r(0)\\) but \\(-\\varepsilon\\notin f_\\varepsilon(\\mathbb D)\\); consequently \\(D_r(0)\\not\\subset f_\\varepsilon(\\mathbb D)\\).  \nThus even with the normalization \\(f'(0)=1\\) no universal \\(r\\) exists.\n\n--------------------------------------------------------------------\n### (c)  An area estimate for functions with a simple pole  \n\nLet  \n\n\\[\nh(z)=\\frac1z+c_0+c_1z+c_2z^2+\\cdots\\qquad (0<|z|<1)\n\\]\n\nbe injective on the punctured disc.  \nFor \\(0<\\rho<1\\) consider the image  \n\n\\[\nh\\bigl(D_\\rho(0)\\setminus\\{0\\}\\bigr).\n\\]\n\nBecause \\(h\\) has a simple pole at \\(0\\) with residue \\(1\\), as \\(|z|\\to0\\) we have \\(h(z)\\to\\infty\\); therefore the complement of this image in \\(\\mathbb C\\) is a bounded set. Its area can be computed by the change\u2011of\u2011variables formula:\n\n\\[\n\\operatorname{Area}\\bigl(\\mathbb C\\setminus h(D_\\rho\\setminus\\{0\\})\\bigr)\n   =\\iint_{|z|>\\rho}|h'(z)|^{2}\\,dA(z),\n\\]\nwhere \\(dA\\) denotes Euclidean area element.\n\nWrite the Laurent series of \\(h'\\):\n\n\\[\nh'(z)=-\\frac1{z^{2}}+c_1+2c_2z+3c_3z^{2}+\\cdots .\n\\]\n\nHence  \n\n\\[\n|h'(z)|^{2}\n   =\\frac1{|z|^{4}}\n     -2\\operatorname{Re}\\!\\Bigl(\\frac{\\overline{c_1}}{z^{2}}\\Bigr)\n     +\\sum_{n\\ge1}n^{2}|c_n|^{2}|z|^{2n-2}\n     +\\text{terms integrating to zero over circles}.\n\\]\n\nIntegrating over the annulus \\(\\rho<|z|<\\infty\\) and using  \n\\(\\displaystyle\\int_{\\rho}^{2\\pi}\\!\\! r^{k}\\,d\\theta\\,dr=\n   \\begin{cases}\n   2\\pi\\frac{\\rho^{k+2}}{k+2}, & k\\neq-2,\\\\[2pt]\n   -2\\pi\\log\\rho, & k=-2,\n   \\end{cases}\\)\nwe obtain  \n\n\\[\n\\operatorname{Area}\\bigl(\\mathbb C\\setminus h(D_\\rho\\setminus\\{0\\})\\bigr)\n   =\\pi\\Bigl(\\frac1{\\rho^{2}}-\\sum_{n\\ge1}n|c_n|^{2}\\rho^{2n}\\Bigr).\n\\]\n\nSince an area is non\u2011negative,  \n\n\\[\n\\sum_{n\\ge1}n|c_n|^{2}\\rho^{2n}\\le\\frac1{\\rho^{2}}\\qquad(0<\\rho<1).\n\\]\n\nLetting \\(\\rho\\to1^{-}\\) (the left\u2013hand side increases with \\(\\rho\\)) gives  \n\n\\[\n\\boxed{\\displaystyle\\sum_{n\\ge1}n|c_n|^{2}\\le1}.\n\\]\n\nThis is Gronwall\u2019s area theorem for functions with a simple pole.\n\n--------------------------------------------------------------------\n### (d)  Constructing the square\u2011root function  \n\nLet  \n\n\\[\nf(z)=z+a_2z^{2}+a_3z^{3}+\\cdots\n\\]\n\nbe injective on \\(\\mathbb D\\) with \\(f(0)=0,\\;f'(0)=1\\).\n\n*Because \\(f\\) is injective and \\(f(0)=0\\), we have \\(f(z)\\neq0\\) for \\(z\\neq0\\).*  \nMoreover  \n\n\\[\n\\frac{f(z)}{z}=1+a_2z+a_3z^{2}+\\cdots\n\\]\n\nis holomorphic on \\(\\mathbb D\\) and equals \\(1\\) at \\(0\\); hence it never vanishes.  \nSince \\(\\mathbb D\\) is simply connected, there exists a holomorphic function \\(\\psi\\) on \\(\\mathbb D\\) such that  \n\n\\[\n\\psi(z)^{2}= \\frac{f(z)}{z},\\qquad \\psi(0)=1 .\n\\]\n\nDefine  \n\n\\[\ng(z)=z\\,\\psi(z^{2}).\n\\]\n\nThen  \n\n\\[\ng(z)^{2}=z^{2}\\psi(z^{2})^{2}=z^{2}\\frac{f(z^{2})}{z^{2}}=f(z^{2}),\n\\]\nso \\(g^{2}(z)=f(z^{2})\\).\n\n*Injectivity of \\(g\\).*  \nIf \\(g(z_{1})=g(z_{2})\\) then squaring gives \\(f(z_{1}^{2})=f(z_{2}^{2})\\); injectivity of \\(f\\) yields \\(z_{1}^{2}=z_{2}^{2}\\), i.e. \\(z_{1}=\\pm z_{2}\\).  \nBut \\(g\\) is odd: \\(g(-z)=-z\\psi(z^{2})=-g(z)\\).  \nHence \\(z_{1}=-z_{2}\\) would imply \\(g(z_{1})=-g(z_{2})\\); equality forces \\(g(z_{2})=0\\), which only happens at \\(z_{2}=0\\) (because \\(g'(0)=1\\neq0\\)). Thus \\(z_{1}=z_{2}\\).  \n\nFinally, \\(g(0)=0\\) and  \n\n\\[\ng'(z)=\\psi(z^{2})+2z^{2}\\psi'(z^{2})\\;\\Longrightarrow\\;g'(0)=\\psi(0)=1 .\n\\]\n\nThus \\(g\\) satisfies the same hypotheses as \\(f\\).\n\n--------------------------------------------------------------------\n### (e)  The second coefficient bound  \n\nFrom the construction in (d),\n\n\\[\n\\psi(z)=\\sqrt{\\frac{f(z)}{z}}\n      =1+\\frac{a_{2}}{2}z+\\Bigl(\\frac{a_{3}}{2}-\\frac{a_{2}^{2}}{8}\\Bigr)z^{2}+\\cdots .\n\\]\n\nHence  \n\n\\[\ng(z)=z\\psi(z^{2})\n    =z\\Bigl(1+\\frac{a_{2}}{2}z^{2}+O(z^{4})\\Bigr)\n    =z+\\frac{a_{2}}{2}z^{3}+O(z^{5}),\n\\]\nso the power series of \\(g\\) is  \n\n\\[\ng(z)=z+b_{2}z^{3}+b_{4}z^{5}+\\cdots ,\\qquad b_{2}=\\frac{a_{2}}{2}.\n\\]\n\nConsequently  \n\n\\[\n\\frac{1}{g(z)}=\\frac1z-b_{2}z+O(z^{3})\n            =\\frac1z-\\frac{a_{2}}{2}z+O(z^{3}).\n\\]\n\nThe function \\(1/g\\) is of the form required in part (c): it is injective on \\(\\mathbb D\\) (because \\(g\\) is) and has a simple pole at \\(0\\) with residue \\(1\\).  \nApplying the estimate of part (c) to \\(1/g\\) gives  \n\n\\[\n\\bigl|-\\tfrac{a_{2}}{2}\\bigr|^{2}\\le 1\\quad\\Longrightarrow\\quad |a_{2}|\\le 2 .\n\\]\n\n*Equality case.*  \nIf \\(|a_{2}|=2\\), then equality holds in the area theorem, which forces the function to have exactly two non\u2011zero coefficients:\n\n\\[\n\\frac{1}{g(z)}=\\frac1z+\\lambda z\\qquad\\text{with }|\\lambda|=1 .\n\\]\n\nThus \\(-\\frac{a_{2}}{2}=\\lambda\\), i.e. \\(a_{2}=-2\\lambda\\).  \nFrom \\(\\frac{1}{g(z)}=\\frac1z+\\lambda z\\) we obtain  \n\n\\[\ng(z)=\\frac{z}{1+\\lambda z^{2}} .\n\\]\n\nNow \\(f(z^{2})=g(z)^{2}= \\dfrac{z^{2}}{(1+\\lambda z^{2})^{2}}\\).  \nReplacing \\(z^{2}\\) by \\(w\\) yields  \n\n\\[\nf(w)=\\frac{w}{(1+\\lambda w)^{2}},\\qquad \\lambda=e^{i\\theta}\\;(\\theta\\in\\mathbb R).\n\\]\n\nHence the extremal functions are precisely the rotations of the Koebe function  \n\n\\[\nf(z)=\\frac{z}{(1-e^{i\\theta}z)^{2}} .\n\\]\n\n--------------------------------------------------------------------\n### (f)  Distance between two omitted values  \n\nLet  \n\n\\[\nh(z)=\\frac1z+c_{0}+c_{1}z+c_{2}z^{2}+\\cdots\n\\]\n\nbe injective on \\(\\mathbb D\\) and assume that \\(h\\) omits the two distinct values \\(z_{1},z_{2}\\).  \nFor \\(j=1,2\\) set  \n\n\\[\nH_{j}(z)=\\frac{1}{h(z)-z_{j}} .\n\\]\n\nBecause \\(h\\) never equals \\(z_{j}\\), each \\(H_{j}\\) is holomorphic on \\(\\mathbb D\\).  \nIf \\(H_{j}(u)=H_{j}(v)\\) then \\(h(u)-z_{j
```
