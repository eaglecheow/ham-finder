export class Client {
  private _id: string;
  public get id(): string {
    return this._id;
  }
  public set id(v: string) {
    this._id = v;
  }

  private _plateNumber: string;
  public get plateNumber(): string {
    return this._plateNumber;
  }
  public set plateNumber(v: string) {
    this._plateNumber = v;
  }
}
