#!/usr/bin/env python3
"""
AXIOM Parser v1.4 - Advanced Word Variation Handling
Final fix for word forms and domain coverage
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

class AdvancedAXIOMParser:
    def __init__(self):
        # Expanded with more variations and domain terms
        self.keyword_mappings = {
            AXIOMNode.INITIATION: ['start', 'begin', 'initiate', 'source', 'origin', 'create', 'generate', 'big bang', 'birth', 'formation', 'emit'],
            AXIOMNode.FLOW: ['flow', 'transfer', 'move', 'current', 'propagate', 'travel', 'transmit', 'orbit', 'revolve', 'circulate', 'stream'],
            AXIOMNode.PROCESSING: ['process', 'transform', 'compute', 'convert', 'calculate', 'change', 'react', 'metabolize', 'digest', 'analyze'],
            AXIOMNode.IMPRINT: ['store', 'remember', 'imprint', 'encode', 'memorize', 'save', 'record', 'learn', 'retain', 'capture', 'memory'],
            AXIOMNode.EMERGENCE: ['emerge', 'create', 'form', 'generate', 'arise', 'become', 'develop', 'consciousness', 'intelligence', 'life'],
            AXIOMNode.CONTAINMENT: ['contain', 'bound', 'limit', 'restrict', 'constrain', 'within', 'stable', 'attract', 'hold', 'capture', 'orbit'],
            AXIOMNode.RECURRENCE: ['repeat', 'cycle', 'oscillate', 'recur', 'periodic', 'rhythm', 'pattern', 'loop', 'heartbeat', 'seasonal'],
            AXIOMNode.IDENTITY: ['identity', 'self', 'essence', 'unique', 'distinct', 'individual', 'character', 'nature'],
            AXIOMNode.POTENTIAL: ['potential', 'capacity', 'ability', 'capability', 'possibility', 'quantum', 'probability', 'latent'],
            AXIOMNode.CONNECTION: ['connect', 'bond', 'link', 'relationship', 'network', 'synapse', 'chemical bond', 'interact']
        }
        
        # Common word variations mapping
        self.word_variations = {
            'memory': ['memories', 'memorization', 'memorize'],
            'cycle': ['cycles', 'cycling', 'cyclical'],
            'flow': ['flows', 'flowing', 'flowed'],
            'process': ['processes', 'processing', 'processed'],
            'transform': ['transforms', 'transforming', 'transformation'],
            'orbit': ['orbits', 'orbiting', 'orbital'],
            'create': ['creates', 'creating', 'creation', 'created'],
            'form': ['forms', 'forming', 'formation', 'formed'],
            'measure': ['measures', 'measuring', 'measurement', 'measured']
        }
    
    def parse_text(self, text: str) -> List[AXIOMNode]:
        symbols = []
        text_lower = text.lower()
        
        for symbol, keywords in self.keyword_mappings.items():
            if any(self._advanced_match(keyword, text_lower) for keyword in keywords):
                if symbol not in symbols:
                    symbols.append(symbol)
                
        return self._apply_natural_flow(symbols)
    
    def _advanced_match(self, keyword: str, text: str) -> bool:
        """Advanced matching with word variations"""
        # Exact match
        if re.search(r'\b' + re.escape(keyword) + r'\b', text):
            return True
        
        # Check known variations
        if keyword in self.word_variations:
            for variation in self.word_variations[keyword]:
                if re.search(r'\b' + re.escape(variation) + r'\b', text):
                    return True
        
        # Common suffix patterns
        suffixes = ['s', 'ing', 'ed', 'ion', 'al', 'ive', 'ment']
        for suffix in suffixes:
            variation = keyword + suffix
            if re.search(r'\b' + re.escape(variation) + r'\b', text):
                return True
                
        return False
    
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

def test_advanced_parser():
    """Test the advanced parser"""
    parser = AdvancedAXIOMParser()
    calculator = STICalculator()
    
    test_cases = [
        "Neurons process information to form memories",
        "Energy flows through ecosystems transforming nutrients",
        "Electrons orbit nucleus creating stable atoms",
        "Water cycles from ocean to clouds to rain and back", 
        "Algorithms process data to generate insights",
        "Quantum particles have potential states until measured",
        "Chemical bonds connect atoms to form molecules",
        "The big bang created the universe which evolved life"
    ]
    
    print("🚀 AXIOM ADVANCED PARSER v1.4 - FINAL FIX")
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
    print("🎯 Advanced parser testing complete!")
    
    # Show improvements
    print("\n📈 KEY IMPROVEMENTS:")
    print("• 'memories' → 'memory' mapping fixed")
    print("• Better word variation handling")
    print("• Maintains all physics improvements")

if __name__ == "__main__":
    test_advanced_parser()
