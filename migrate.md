#### Migrate a Resource
There is now a way to migrate existing registered DiGIR, BioCASE, TAPIR, or DwC-A resources to an IPT. This allows the existing resource to preserve its GBIF Registry UUID.

The way this works, is that the IPT resource is configured to update the existing registered resource that it corresponds to in the GBIF Registry. 

To migrate an **existing registered resource** to your **IPT resource**, simply follow these instructions:

1. Ensure that the **IPT resource's** visibility is public and NOT registered.
2. Determine the owning organisation of the e**xisting registered resource**, and ensure that it is added to the IPT as an organisation, and that it is configured to publish datasets. To do so, please refer to the section "Add Organisation".
3. Select the owning organisation from the drop-down list on the Basic Metadata page. Don't forget to save the Basic Metadata page.
4. Go to the GBIF Dataset page of the **existing registered resource**. Depending on whether you are running the IPT in test or production mode, you would visit <a href='http://www.gbif-uat.org/dataset'>http://www.gbif-uat.org/dataset</a> or <a href='http://www.gbif.org/dataset'>http://www.gbif.org/dataset</a> respectively. 
5. Ensure GBIF Dataset page shows the correct **owning organisation** of the **existing registered resource**. Warning: if it shows a different **owning organisation**, the GBIF Registry must be updated before you can proceed with the remaining steps. Send an email to helpdesk@gbif.org alerting them to the update needed.
6. Copy the GBIF Registry UUID from the GBIF Dataset page URL, e.g "5d637678-cb64-4863-a12b-78b4e1a56628". 
7. Add this UUID to the list of the **IPT resource's** alternative identifiers on the Additional Metadata page. Don't forget to save the Additional Metadata page.
8. Ensure that no other public or registered resource in your IPT includes this UUID in their list of alternative identifiers. In cases where you are trying to replace a registered resource that already exists in your IPT, the other resource has to be deleted first.
9. On the resource overview page, click the register button. Similar to any other registration, you will have to confirm that you have read and understood the GBIF data sharing agreement before the registration will be executed.
10. **Send an email to helpdesk@gbif.org alerting them about the update**. In your email please enclose:
  1. the name and URL (or GBIF Registry UUID) of your IPT
  2. the name and GBIF Registry UUID of your updated Resource (see line Resource Key on resource overview page, for example: Resource Key d990532f-6783-4871-b2d3-cae3d0cb872b)
  3. (if applicable) whether the DiGIR/BioCASE/TAPIR technical installation that used to serve the resource has been deprecated, and whether it can be deleted from the GBIF Registry
