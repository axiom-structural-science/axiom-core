#!/usr/bin/env python3
"""
AXIOM Enhanced Parser v1.2
Domain-specific keyword expansion for better symbol detection
"""

from enum import Enum
from typing import List, Dict
import re

class AXIOMNode(str, Enum):
    INITIATION = "│"
    POTENTIAL = "¬"
    FLOW = "⌒"
    PROCESSING = "█"
    RAW_FORCE = "┼"
    IMPRINT = "┴"
    CONTAINMENT = "—"
    RECURRENCE = "┘"
    EMERGENCE = "┬"
    RETURN = "⌑"
    FOCUS = "◆"
    MANIFESTATION = "┌"
    DOMAIN = "└"
    EMISSION = "┐"
    GUIDANCE = "├"
    CONNECTION = "┤"
    SYNCHRONIZATION = "≡"
    IDENTITY = "⟦⟧"

class EnhancedAXIOMParser:
    def __init__(self):
        # Expanded keyword mappings with domain-specific terms
        self.keyword_mappings = {
            AXIOMNode.INITIATION: [
                'start', 'begin', 'initiate', 'source', 'origin', 'create', 'generate',
                'big bang', 'birth', 'formation', 'emit', 'release', 'produce'
            ],
            AXIOMNode.FLOW: [
                'flow', 'transfer', 'move', 'current', 'propagate', 'travel', 'transmit',
                'orbit', 'revolve', 'circulate', 'stream', 'pass', 'spread', 'diffuse',
                'conduct', 'convey', 'channel'
            ],
            AXIOMNode.PROCESSING: [
                'process', 'transform', 'compute', 'convert', 'calculate', 'change',
                'react', 'metabolize', 'digest', 'analyze', 'synthesize', 'modify',
                'adapt', 'evolve', 'learn', 'adjust'
            ],
            AXIOMNode.IMPRINT: [
                'store', 'remember', 'imprint', 'encode', 'memorize', 'save', 'record',
                'learn', 'retain', 'capture', 'encode', 'pattern', 'memory', 'engram',
                'crystalize', 'solidify'
            ],
            AXIOMNode.EMERGENCE: [
                'emerge', 'create', 'form', 'generate', 'arise', 'become', 'develop',
                'consciousness', 'intelligence', 'life', 'complexity', 'self-organize',
                'appear', 'manifest', 'arise', 'result'
            ],
            AXIOMNode.CONTAINMENT: [
                'contain', 'bound', 'limit', 'restrict', 'constrain', 'within',
                'stable', 'attract', 'hold', 'capture', 'trap', 'confine', 'enclose',
                'orbit', 'gravitational', 'magnetic', 'cell membrane', 'barrier'
            ],
            AXIOMNode.RECURRENCE: [
                'repeat', 'cycle', 'oscillate', 'recur', 'periodic', 'rhythm',
                'pattern', 'loop', 'heartbeat', 'seasonal', 'daily', 'annual',
                'feedback', 'resonate', 'pulse', 'vibrate'
            ],
            AXIOMNode.IDENTITY: [
                'identity', 'self', 'essence', 'unique', 'distinct', 'individual',
                'character', 'nature', 'personality', 'species', 'type', 'kind',
                'quantum state', 'eigenstate', 'signature'
            ],
            AXIOMNode.POTENTIAL: [
                'potential', 'capacity', 'ability', 'capability', 'possibility',
                'quantum', 'probability', 'may', 'could', 'might', 'latent',
                'unexpressed', 'dormant', 'inherent'
            ],
            AXIOMNode.CONNECTION: [
                'connect', 'bond', 'link', 'relationship', 'network', 'synapse',
                'chemical bond', 'social', 'interact', 'communicate', 'associate',
                'correlate', 'relate'
            ]
        }
    
    def parse_text(self, text: str) -> List[AXIOMNode]:
        symbols = []
        text_lower = text.lower()
        
        for symbol, keywords in self.keyword_mappings.items():
            if any(self._word_in_text(keyword, text_lower) for keyword in keywords):
                if symbol not in symbols:  # Avoid duplicates
                    symbols.append(symbol)
                
        return self._apply_natural_flow(symbols)
    
    def _word_in_text(self, word: str, text: str) -> bool:
        """Check if word appears as whole word in text"""
        return re.search(r'\b' + re.escape(word) + r'\b', text) is not None
    
    def _apply_natural_flow(self, symbols: List[AXIOMNode]) -> List[AXIOMNode]:
        natural_order = [
            AXIOMNode.INITIATION, AXIOMNode.FLOW, AXIOMNode.PROCESSING,
            AXIOMNode.IMPRINT, AXIOMNode.EMERGENCE, AXIOMNode.CONTAINMENT,
            AXIOMNode.RECURRENCE, AXIOMNode.RETURN
        ]
        
        ordered_symbols = [s for s in natural_order if s in symbols]
        remaining_symbols = [s for s in symbols if s not in natural_order]
        
        return ordered_symbols + remaining_symbols

class STICalculator:
    def __init__(self):
        self.nsf_weights = {
            AXIOMNode.INITIATION: 1.0,
            AXIOMNode.FLOW: 1.2, 
            AXIOMNode.PROCESSING: 1.5,
            AXIOMNode.IMPRINT: 1.1,
            AXIOMNode.EMERGENCE: 1.4,
            AXIOMNode.CONTAINMENT: 1.0,
            AXIOMNode.RECURRENCE: 1.1,
            AXIOMNode.RETURN: 1.0
        }
        
        self.nsf_core_nodes = list(self.nsf_weights.keys())
    
    def calculate_sti(self, symbols: List[AXIOMNode]) -> Dict:
        present_nodes = [s for s in symbols if s in self.nsf_core_nodes]
        missing_nodes = [s for s in self.nsf_core_nodes if s not in symbols]
        
        total_weight = sum(self.nsf_weights.values())
        missing_weight = sum(self.nsf_weights[node] for node in missing_nodes)
        
        sti_score = 1 - (missing_weight / total_weight)
        
        return {
            'symbols': symbols,
            'missing_nodes': missing_nodes,
            'sti_score': round(sti_score, 3),
            'present_nodes': present_nodes
        }

def test_enhanced_parser():
    """Test the enhanced parser with our previous examples"""
    parser = EnhancedAXIOMParser()
    calculator = STICalculator()
    
    test_cases = [
        "Neurons process information to form memories",
        "Energy flows through ecosystems transforming nutrients",
        "Electrons orbit nucleus creating stable atoms",
        "Water cycles from ocean to clouds to rain and back", 
        "Algorithms process data to generate insights",
        # New test cases
        "Quantum particles have potential states until measured",
        "Chemical bonds connect atoms to form molecules",
        "The big bang created the universe which evolved life"
    ]
    
    print("🚀 AXIOM ENHANCED PARSER v1.2 - DOMAIN TESTING")
    print("=" * 60)
    
    for i, text in enumerate(test_cases, 1):
        symbols = parser.parse_text(text)
        result = calculator.calculate_sti(symbols)
        
        print(f"\n{i}. {text}")
        print(f"   🔍 Symbols: {''.join(symbols)}")
        print(f"   📊 STI: {result['sti_score']}")
        
        if result['missing_nodes']:
            print(f"   ⚠️  Missing: {', '.join(result['missing_nodes'])}")
        else:
            print("   ✅ Structurally complete!")
    
    print("\n" + "=" * 60)
    print("🎯 Enhanced parser testing complete!")

def main():
    """Interactive version for user input"""
    parser = EnhancedAXIOMParser()
    calculator = STICalculator()
    
    print("🌌 AXIOM Enhanced Structural Analysis v1.2")
    print("=" * 50)
    
    while True:
        text = input("\n📝 Enter system description (or 'quit'): ")
        
        if text.lower() == 'quit':
            break
            
        symbols = parser.parse_text(text)
        result = calculator.calculate_sti(symbols)
        
        print(f"\n🔍 Found Symbols: {''.join(result['symbols'])}")
        print(f"📊 STI Score: {result['sti_score']}")
        
        if result['missing_nodes']:
            print(f"⚠️  Missing: {', '.join(result['missing_nodes'])}")
        else:
            print("✅ Structurally complete!")
            
        print("-" * 50)

if __name__ == "__main__":
    # Run tests automatically
    test_enhanced_parser()
    
    # Then start interactive mode
    print("\n" + "=" * 60)
    main()
