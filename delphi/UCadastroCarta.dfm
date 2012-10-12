object frmCadastroCarta: TfrmCadastroCarta
  Left = 0
  Top = 0
  BorderStyle = bsDialog
  Caption = 'Cadastro Carta'
  ClientHeight = 502
  ClientWidth = 726
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  Position = poDesktopCenter
  OnCreate = FormCreate
  PixelsPerInch = 96
  TextHeight = 13
  object imgCard: TcxDBImage
    Left = 512
    Top = 34
    Hint = 'Selecionar Imagem'
    AutoSize = True
    DataBinding.DataField = 'image'
    DataBinding.DataSource = dsCard
    ShowHint = True
    TabOrder = 0
    OnClick = imgCardClick
    Height = 201
    Width = 140
  end
  object edtNome: TcxDBTextEdit
    Left = 24
    Top = 34
    DataBinding.DataField = 'nome'
    DataBinding.DataSource = dsCard
    TabOrder = 1
    Width = 225
  end
  object cxLabel1: TcxLabel
    Left = 24
    Top = 16
    Caption = 'Nome'
    Transparent = True
  end
  object edtCodigo: TcxDBTextEdit
    Left = 255
    Top = 34
    DataBinding.DataField = 'codigo'
    DataBinding.DataSource = dsCard
    TabOrder = 3
    Width = 146
  end
  object cxLabel2: TcxLabel
    Left = 255
    Top = 16
    Caption = 'C'#243'digo'
    Transparent = True
  end
  object cxLabel3: TcxLabel
    Left = 24
    Top = 58
    Caption = 'Categoria'
    Transparent = True
  end
  object edtNivel: TcxDBTextEdit
    Left = 26
    Top = 124
    DataBinding.DataField = 'nivel'
    DataBinding.DataSource = dsCard
    TabOrder = 6
    Width = 49
  end
  object cxLabel4: TcxLabel
    Left = 26
    Top = 106
    Caption = 'N'#237'vel'
    Transparent = True
  end
  object edtTipo: TcxDBTextEdit
    Left = 255
    Top = 79
    DataBinding.DataField = 'tipo'
    DataBinding.DataSource = dsCard
    TabOrder = 8
    Width = 146
  end
  object cxLabel5: TcxLabel
    Left = 255
    Top = 61
    Caption = 'Tipo'
    Transparent = True
  end
  object cmbCategoria: TcxDBComboBox
    Left = 24
    Top = 79
    DataBinding.DataField = 'categoria'
    DataBinding.DataSource = dsCard
    Properties.Items.Strings = (
      'Monster'
      'Spell'
      'Trap')
    Properties.OnChange = cmbCategoriaPropertiesChange
    TabOrder = 10
    Width = 225
  end
  object edtATK: TcxDBTextEdit
    Left = 208
    Top = 124
    DataBinding.DataField = 'ataque'
    DataBinding.DataSource = dsCard
    TabOrder = 11
    Width = 92
  end
  object cxLabel6: TcxLabel
    Left = 208
    Top = 108
    Caption = 'ATK'
    Transparent = True
  end
  object edtDEF: TcxDBTextEdit
    Left = 307
    Top = 124
    DataBinding.DataField = 'defesa'
    DataBinding.DataSource = dsCard
    TabOrder = 13
    Width = 94
  end
  object cxLabel7: TcxLabel
    Left = 81
    Top = 107
    Caption = 'Atributo'
    Transparent = True
  end
  object cmbAtributo: TcxDBComboBox
    Left = 81
    Top = 124
    DataBinding.DataField = 'atributo'
    DataBinding.DataSource = dsCard
    Properties.Items.Strings = (
      'Dark'
      'Light'
      'Earth'
      'Wind'
      'Fire'
      'Water')
    TabOrder = 15
    Width = 121
  end
  object cxLabel8: TcxLabel
    Left = 307
    Top = 106
    Caption = 'DEF'
    Transparent = True
  end
  object btnIncluir: TcxButton
    Left = 186
    Top = 251
    Width = 75
    Height = 25
    Caption = 'Incluir'
    TabOrder = 17
    OnClick = btnIncluirClick
  end
  object btnSalvar: TcxButton
    Left = 267
    Top = 251
    Width = 75
    Height = 25
    Caption = 'Salvar'
    TabOrder = 18
    OnClick = btnSalvarClick
  end
  object btnCancelar: TcxButton
    Left = 348
    Top = 251
    Width = 75
    Height = 25
    Caption = 'Cancelar'
    TabOrder = 19
    OnClick = btnCancelarClick
  end
  object btnRemover: TcxButton
    Left = 429
    Top = 251
    Width = 75
    Height = 25
    Caption = 'Remover'
    TabOrder = 20
    OnClick = btnRemoverClick
  end
  object memoDescricao: TcxDBMemo
    Left = 24
    Top = 170
    DataBinding.DataField = 'descricao'
    DataBinding.DataSource = dsCard
    TabOrder = 21
    Height = 65
    Width = 377
  end
  object cxLabel9: TcxLabel
    Left = 24
    Top = 152
    Caption = 'Descri'#231#227'o'
    Transparent = True
  end
  object Grid: TcxGrid
    Left = 0
    Top = 290
    Width = 726
    Height = 212
    Align = alBottom
    TabOrder = 23
    ExplicitTop = 288
    ExplicitWidth = 576
    object GridDBTableView1: TcxGridDBTableView
      NavigatorButtons.ConfirmDelete = False
      DataController.DataSource = dsCard
      DataController.Summary.DefaultGroupSummaryItems = <>
      DataController.Summary.FooterSummaryItems = <>
      DataController.Summary.SummaryGroups = <>
      OptionsData.Editing = False
      OptionsSelection.CellSelect = False
      OptionsView.GroupByBox = False
      object GridDBTableView1nome: TcxGridDBColumn
        Caption = 'Nome'
        DataBinding.FieldName = 'nome'
        Width = 243
      end
      object GridDBTableView1codigo: TcxGridDBColumn
        Caption = 'C'#243'digo'
        DataBinding.FieldName = 'codigo'
        Width = 76
      end
      object GridDBTableView1categoria: TcxGridDBColumn
        Caption = 'Categoria'
        DataBinding.FieldName = 'categoria'
        Width = 69
      end
      object GridDBTableView1tipo: TcxGridDBColumn
        Caption = 'Tipo'
        DataBinding.FieldName = 'tipo'
        Width = 79
      end
      object GridDBTableView1nivel: TcxGridDBColumn
        Caption = 'N'#237'vel'
        DataBinding.FieldName = 'nivel'
      end
      object GridDBTableView1atributo: TcxGridDBColumn
        Caption = 'Atributo'
        DataBinding.FieldName = 'atributo'
      end
      object GridDBTableView1ataque: TcxGridDBColumn
        Caption = 'ATK'
        DataBinding.FieldName = 'ataque'
      end
      object GridDBTableView1defesa: TcxGridDBColumn
        Caption = 'DEF'
        DataBinding.FieldName = 'defesa'
      end
    end
    object GridLevel1: TcxGridLevel
      GridView = GridDBTableView1
    end
  end
  object qryCard: TADOQuery
    Connection = DTM.Connection
    CursorType = ctStatic
    Parameters = <>
    SQL.Strings = (
      'Select * from cards')
    Left = 472
    Top = 240
    object qryCardid: TAutoIncField
      FieldName = 'id'
      ReadOnly = True
    end
    object qryCardnome: TStringField
      FieldName = 'nome'
      Size = 60
    end
    object qryCardcodigo: TStringField
      FieldName = 'codigo'
      Size = 10
    end
    object qryCarddescricao: TMemoField
      FieldName = 'descricao'
      BlobType = ftMemo
    end
    object qryCardnivel: TIntegerField
      FieldName = 'nivel'
    end
    object qryCardtipo: TStringField
      FieldName = 'tipo'
      Size = 45
    end
    object qryCardatributo: TStringField
      FieldName = 'atributo'
      Size = 10
    end
    object qryCardataque: TIntegerField
      FieldName = 'ataque'
    end
    object qryCarddefesa: TIntegerField
      FieldName = 'defesa'
    end
    object qryCardcategoria: TStringField
      FieldName = 'categoria'
      Size = 10
    end
    object qryCardimage: TBlobField
      FieldName = 'image'
    end
  end
  object dsCard: TDataSource
    DataSet = qryCard
    OnStateChange = dsCardStateChange
    Left = 520
    Top = 240
  end
  object OpenDialog: TOpenDialog
    Left = 392
    Top = 8
  end
end
