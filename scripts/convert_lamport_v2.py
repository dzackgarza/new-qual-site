#!/usr/bin/env python3
"""Convert typed-step proofs to lamport_proof.lua filter syntax.

This handles the actual format where <1>1. appears on the same line as the claim.
"""
import re
import sys
from pathlib import Path
from typing import List, Tuple


def find_solution_blocks(lines: List[str]) -> List[Tuple[int, int]]:
    """Find (start, end) indices of solution/proof/hint blocks."""
    blocks = []
    i = 0
    while i < len(lines):
        if re.match(r'^:::\s*\{?\.(solution|proof|hint)\}?', lines[i]):
            start = i
            depth = 1
            i += 1
            while i < len(lines) and depth > 0:
                if re.match(r'^:::\s*\{?\.\w+', lines[i]):
                    depth += 1
                elif lines[i].strip() == ':::':
                    depth -= 1
                    if depth == 0:
                        blocks.append((start, i))
                        break
                i += 1
        i += 1
    return blocks


def has_typed_steps(lines: List[str], start: int, end: int) -> bool:
    """Check if a block has typed step markers."""
    for i in range(start, end + 1):
        if re.search(r'<\d+>\d+\.', lines[i]):
            return True
    return False


def convert_block(lines: List[str], start: int, end: int) -> List[str]:
    """Convert a solution block with typed steps to pf syntax."""
    result = []
    i = start + 1  # Skip opening :::
    
    # Collect pre-proof content (notation, setup)
    pre_proof = []
    while i < end:
        if re.match(r'^<\d+>\d+\.', lines[i]):
            break
        pre_proof.append(lines[i])
        i += 1
    
    # Add pre-proof content before ::: pf
    result.extend(pre_proof)
    if pre_proof and pre_proof[-1].strip():
        result.append('\n')
    
    result.append('::: pf\n')
    result.append('\n')
    
    # Process steps
    steps = collect_steps(lines, i, end)
    result.extend(convert_steps(steps, 1))
    
    result.append(':::\n')
    
    return result


def collect_steps(lines: List[str], start: int, end: int) -> List[dict]:
    """Collect all steps with their structure."""
    steps = []
    i = start
    
    while i < end:
        match = re.match(r'^<(\d+)>(\d+)\.\s*(.*)', lines[i])
        if match:
            level = int(match.group(1))
            num = int(match.group(2))
            first_line = match.group(3)
            
            # Check if this is Q.E.D.
            is_qed = first_line.strip() in ['Q.E.D.', 'Q.E.D', ''] and num > 1
            
            # Collect claim lines until next step or proof block
            claim = [first_line + '\n'] if first_line.strip() else []
            i += 1
            
            while i < end:
                if re.match(r'^<\d+>\d+\.', lines[i]):
                    break
                if re.match(r'^:::\s*\{?\.?proof\}?', lines[i]):
                    break
                claim.append(lines[i])
                i += 1
            
            # Remove trailing empty lines from claim
            while claim and not claim[-1].strip():
                claim.pop()
            
            # Check for proof block
            proof_lines = []
            if i < end and re.match(r'^:::\s*\{?\.?proof\}?', lines[i]):
                i += 1  # Skip ::: {.proof}
                while i < end and lines[i].strip() != ':::':
                    proof_lines.append(lines[i])
                    i += 1
                if i < end:
                    i += 1  # Skip closing :::
            
            steps.append({
                'level': level,
                'num': num,
                'is_qed': is_qed,
                'claim': claim,
                'proof': proof_lines
            })
        else:
            i += 1
    
    return steps


def convert_steps(steps: List[dict], current_level: int) -> List[str]:
    """Convert steps at current level and recurse for substeps."""
    result = []
    i = 0
    
    while i < len(steps):
        step = steps[i]
        
        if step['level'] < current_level:
            # Step from parent level, shouldn't happen in well-formed input
            i += 1
            continue
        elif step['level'] > current_level:
            # This is a substep of the previous step, already handled
            i += 1
            continue
        
        # This step is at current level
        if step['is_qed']:
            result.append('::: pf-qed\n')
            result.append('\n')
            
            # Add proof content without recursion (Q.E.D. doesn't have substeps)
            for line in step['proof']:
                # Remove references to "Q.E.D." text
                if not re.match(r'^\s*Q\.E\.D\.\s*$', line):
                    result.append(line)
            
            result.append('\n')
            result.append(':::\n')
            result.append('\n')
        else:
            result.append('::: pf-step\n')
            result.append('\n')
            
            # Add claim
            for line in step['claim']:
                result.append(line)
            if step['claim']:
                result.append('\n')
            
            # Check if there are substeps in the proof
            substeps = []
            next_level = current_level + 1
            j = i + 1
            while j < len(steps) and steps[j]['level'] >= next_level:
                if steps[j]['level'] == next_level:
                    substeps.append(steps[j])
                j += 1
            
            if step['proof'] or substeps:
                result.append('\n')
                result.append('::: pf-proof\n')
                result.append('\n')
                
                if substeps:
                    # Add proof prose before substeps
                    prose_lines = []
                    for line in step['proof']:
                        if not re.match(r'^<\d+>\d+\.', line):
                            prose_lines.append(line)
                    for line in prose_lines:
                        result.append(line)
                    if prose_lines and prose_lines[-1].strip():
                        result.append('\n')
                    
                    # Convert substeps
                    result.extend(convert_steps(substeps, next_level))
                    i = j - 1  # Skip substeps we just processed
                else:
                    # Just prose
                    for line in step['proof']:
                        result.append(line)
                    if step['proof'] and step['proof'][-1].strip():
                        result.append('\n')
                
                result.append(':::\n')
                result.append('\n')
            
            result.append(':::\n')
            result.append('\n')
        
        i += 1
    
    return result


def convert_file(filepath: Path) -> bool:
    """Convert typed steps in a file to pf syntax. Returns True if modified."""
    try:
        content = filepath.read_text()
        lines = content.splitlines(keepends=True)
        
        blocks = find_solution_blocks(lines)
        if not blocks:
            return False
        
        # Check if any block has typed steps
        has_work = False
        for start, end in blocks:
            if has_typed_steps(lines, start, end):
                has_work = True
                break
        
        if not has_work:
            return False
        
        # Convert blocks in reverse order to preserve indices
        for start, end in reversed(blocks):
            if has_typed_steps(lines, start, end):
                converted = convert_block(lines, start, end)
                lines[start:end+1] = converted
        
        filepath.write_text(''.join(lines))
        return True
    except Exception as e:
        print(f"Error converting {filepath}: {e}", file=sys.stderr)
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: convert_lamport_v2.py <file1> [file2 ...]", file=sys.stderr)
        sys.exit(1)
    
    converted = 0
    skipped = 0
    
    for filepath in sys.argv[1:]:
        path = Path(filepath)
        if not path.exists():
            print(f"Not found: {filepath}", file=sys.stderr)
            continue
        
        if convert_file(path):
            converted += 1
            print(f"✓ {filepath}")
        else:
            skipped += 1
    
    print(f"\nConverted: {converted}, Skipped: {skipped}", file=sys.stderr)


if __name__ == '__main__':
    main()
