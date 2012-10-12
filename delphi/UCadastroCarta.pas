unit UCadastroCarta;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, cxGraphics, cxControls, cxLookAndFeels, cxLookAndFeelPainters,
  cxContainer, cxEdit, dxSkinsCore, dxSkinBlack, dxSkinBlue, dxSkinCaramel,
  dxSkinCoffee, dxSkinDarkRoom, dxSkinDarkSide, dxSkinFoggy, dxSkinGlassOceans,
  dxSkiniMaginary, dxSkinLilian, dxSkinLiquidSky, dxSkinLondonLiquidSky,
  dxSkinMcSkin, dxSkinMoneyTwins, dxSkinOffice2007Black, dxSkinOffice2007Blue,
  dxSkinOffice2007Green, dxSkinOffice2007Pink, dxSkinOffice2007Silver,
  dxSkinOffice2010Black, dxSkinOffice2010Blue, dxSkinOffice2010Silver,
  dxSkinPumpkin, dxSkinSeven, dxSkinSharp, dxSkinSilver, dxSkinSpringTime,
  dxSkinStardust, dxSkinSummer2008, dxSkinsDefaultPainters, dxSkinValentine,
  dxSkinXmas2008Blue, Menus, StdCtrls, cxButtons, cxMaskEdit, cxDropDownEdit,
  cxDBEdit, DB, cxLabel, cxTextEdit, cxImage, ADODB, cxStyles,
  dxSkinscxPCPainter, cxCustomData, cxFilter, cxData, cxDataStorage, cxDBData,
  cxGridCustomTableView, cxGridTableView, cxGridDBTableView, cxGridLevel,
  cxClasses, cxGridCustomView, cxGrid, cxMemo;

type
  TfrmCadastroCarta = class(TForm)
    qryCard: TADOQuery;
    qryCardid: TAutoIncField;
    qryCardnome: TStringField;
    qryCardcodigo: TStringField;
    qryCarddescricao: TMemoField;
    qryCardnivel: TIntegerField;
    qryCardtipo: TStringField;
    qryCardatributo: TStringField;
    qryCardataque: TIntegerField;
    qryCarddefesa: TIntegerField;
    qryCardcategoria: TStringField;
    qryCardimage: TBlobField;
    imgCard: TcxDBImage;
    edtNome: TcxDBTextEdit;
    cxLabel1: TcxLabel;
    dsCard: TDataSource;
    edtCodigo: TcxDBTextEdit;
    cxLabel2: TcxLabel;
    cxLabel3: TcxLabel;
    edtNivel: TcxDBTextEdit;
    cxLabel4: TcxLabel;
    edtTipo: TcxDBTextEdit;
    cxLabel5: TcxLabel;
    cmbCategoria: TcxDBComboBox;
    edtATK: TcxDBTextEdit;
    cxLabel6: TcxLabel;
    edtDEF: TcxDBTextEdit;
    cxLabel7: TcxLabel;
    cmbAtributo: TcxDBComboBox;
    cxLabel8: TcxLabel;
    btnIncluir: TcxButton;
    btnSalvar: TcxButton;
    btnCancelar: TcxButton;
    btnRemover: TcxButton;
    memoDescricao: TcxDBMemo;
    cxLabel9: TcxLabel;
    GridDBTableView1: TcxGridDBTableView;
    GridLevel1: TcxGridLevel;
    Grid: TcxGrid;
    GridDBTableView1nome: TcxGridDBColumn;
    GridDBTableView1codigo: TcxGridDBColumn;
    GridDBTableView1nivel: TcxGridDBColumn;
    GridDBTableView1tipo: TcxGridDBColumn;
    GridDBTableView1atributo: TcxGridDBColumn;
    GridDBTableView1ataque: TcxGridDBColumn;
    GridDBTableView1defesa: TcxGridDBColumn;
    GridDBTableView1categoria: TcxGridDBColumn;
    OpenDialog: TOpenDialog;
    procedure btnIncluirClick(Sender: TObject);
    procedure btnSalvarClick(Sender: TObject);
    procedure btnCancelarClick(Sender: TObject);
    procedure btnRemoverClick(Sender: TObject);
    procedure cmbCategoriaPropertiesChange(Sender: TObject);
    procedure dsCardStateChange(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure imgCardClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  frmCadastroCarta: TfrmCadastroCarta;

implementation

uses UDataBase;

{$R *.dfm}

procedure TfrmCadastroCarta.btnCancelarClick(Sender: TObject);
begin
   if MessageDlg('Existem altera��es n�o salvas, deseja cancelar?',
   mtConfirmation, mbYesNo, 0) = mrYes then
      qryCard.Cancel;


end;

procedure TfrmCadastroCarta.btnIncluirClick(Sender: TObject);
begin
   qryCard.Append;
end;

procedure TfrmCadastroCarta.btnRemoverClick(Sender: TObject);
begin
   if MessageDlg('Deseja remover a carta?', mtConfirmation, mbYesNo, 0) = mrYes then
      qryCard.Delete;
end;

procedure TfrmCadastroCarta.btnSalvarClick(Sender: TObject);
begin
   try
      qryCard.Post
   Except on E:Exception do
      ShowMessage(E.Message);
   end;
end;

procedure TfrmCadastroCarta.cmbCategoriaPropertiesChange(Sender: TObject);
begin
   if qryCardcategoria.AsString = 'Monster' then
   begin
      edtNivel.Enabled := True;
      edtATK.Enabled := True;
      edtDEF.Enabled := True;
      cmbAtributo.Enabled := True;
   end else
   begin
      edtNivel.Enabled := False;
      edtATK.Enabled := False;
      edtDEF.Enabled := False;
      cmbAtributo.Enabled := False;
   end;
end;

procedure TfrmCadastroCarta.dsCardStateChange(Sender: TObject);
begin
   if dsCard.State in [dsInsert, dsEdit] then
   begin
      btnIncluir.Enabled := False;
      btnRemover.Enabled := False;
      btnSalvar.Enabled := True;
      btnCancelar.Enabled := True;
   end else
   begin
      btnIncluir.Enabled := True;
      btnRemover.Enabled := True;
      btnSalvar.Enabled := False;
      btnCancelar.Enabled := False;
   end;
end;

procedure TfrmCadastroCarta.FormCreate(Sender: TObject);
begin
   qryCard.Active := True;
end;

procedure TfrmCadastroCarta.imgCardClick(Sender: TObject);
begin
   if not (dsCard.State in [dsInsert, dsEdit]) then
      qryCard.Edit;


   OpenDialog.DefaultExt := 'bmp';
   OpenDialog.Title := 'Abrir Imagem da Carta';

   if OpenDialog.Execute then
   begin
      imgCard.Picture.LoadFromFile(OpenDialog.FileName);
      (qryCardimage as TBlobField).LoadFromFile(OpenDialog.FileName);
   end;
end;

end.
