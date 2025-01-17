#RUN FIFTH

from TAC_Generator import tac_code

class AssemblyCodeGenerator:
    def __init__(self):
        self.assembly_code=[]
        self.register_pool=["rax","rbx","rcx","rdx"] #available registers
        self.var_to_reg={}

    def generate(self,tac_code):
        for instruction in tac_code:
            self.translate_instruction(instruction)
        return self.assembly_code
    
    def translate_instruction(self , instruction):
        parts=instruction.split()
        if len(parts)==5:
            dest , _ , src1 , op , src2 =parts
            self.emit_operation(dest , src1 , op , src2)
        else:
            raise ValueError(f"Unsupported TAC Instruction: {instruction}")
    
    def emit_operation(self,dest,src1,op,src2):
        reg1=self.allocate_register(src1)
        self.assembly_code.append(f"MOV {reg1} ,[{src1}]")

        reg2=self.allocate_register(src2)
        self.assembly_code.append(f"MOV {reg2} ,[{src2}]")

        if op=='+':
            self.assembly_code.append(f"ADD {reg1} ,{reg2}")
        elif op=='-':
            self.assembly_code.append(f"SUB {reg1} ,{reg2}")
        elif op=='*':
            self.assembly_code.append(f"IMUL {reg1} ,{reg2}")
        elif op=='/':
            self.assembly_code.append(f"IDIV {reg2}")
        else:
            raise ValueError(f"Unsupported Operation :  {op}")
        
        self.assembly_code.append(f"MOV [{dest}] , {reg1}")

        self.free_register(reg1)
        self.free_register(reg2)


    def allocate_register(self,var):
        if var in self.var_to_reg:
            return self.var_to_reg[var]
        if not self.register_pool:
            raise RuntimeError("No registers Available")
        reg=self.register_pool.pop(0)
        self.var_to_reg[var]=reg
        return reg
    
    def free_register(self,reg):
        if reg in self.register_pool:
            return
        self.register_pool.append(reg)
        for var,r in list(self.var_to_reg.items()):
            if r==reg:
                del self.var_to_reg[var]

    def get_assembly_code(self):
        return "\n".join(self.assembly_code)
    



asm_generator=AssemblyCodeGenerator()
asm_generator.generate(tac_code)
print(asm_generator.get_assembly_code())