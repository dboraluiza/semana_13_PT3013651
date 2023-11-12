class AlunoClass:

  def __init__(self, nome, sobrenome, nota):
    self.nome = nome
    self.sobrenome = sobrenome
    self.nota = nota

  def mostrarAluno(self):
    return 'Aluno: ' + self.nome + ' ' + self.sobrenome + ' - Nota: ' + str(
      self.nota)

  def salvar(self, conexao, colecao):
    dados_aluno = {
      'nome': self.nome,
      'sobrenome': self.sobrenome,
      'nota': self.nota
    }
    resultado = conexao[colecao].insert_one(dados_aluno)
    return resultado.acknowledged
